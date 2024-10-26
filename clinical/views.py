from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.cache import cache
from .models import Patient, ClinicalNote, Order, Task, AuditLog
from .forms import PatientForm, ClinicalNoteForm, OrderForm, TaskForm, PatientSearchForm

@login_required
def patient_list(request):
    form = PatientSearchForm(request.GET)
    patients = Patient.objects.all().order_by('-created_at')

    if form.is_valid():
        query = form.cleaned_data.get('search_query')
        date_from = form.cleaned_data.get('date_from')
        date_to = form.cleaned_data.get('date_to')

        if query:
            patients = patients.filter(
                Q(name__icontains=query) |
                Q(patient_id__icontains=query) |
                Q(medical_history__icontains=query)
            )

        if date_from:
            patients = patients.filter(created_at__gte=date_from)
        if date_to:
            patients = patients.filter(created_at__lte=date_to)

    paginator = Paginator(patients, 10)
    page = request.GET.get('page')
    patients = paginator.get_page(page)

    return render(request, 'clinical/patient_list.html', {
        'patients': patients,
        'form': form
    })

@login_required
def patient_detail(request, pk):
    cache_key = f'patient_{pk}'
    patient = cache.get(cache_key)

    if not patient:
        patient = get_object_or_404(
            Patient.objects.prefetch_related('notes', 'order_set'),
            pk=pk
        )
        cache.set(cache_key, patient, 300)  # Cache for 5 minutes

    if request.method == 'POST':
        form = ClinicalNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.patient = patient
            note.created_by = request.user
            note.save()
            messages.success(request, 'Clinical note added successfully!')
            cache.delete(cache_key)  # Invalidate cache
            return redirect('patient_detail', pk=pk)
    else:
        form = ClinicalNoteForm()

    return render(request, 'clinical/patient_detail.html', {
        'patient': patient,
        'form': form
    })

@login_required
def patient_create(request):
    try:
        if request.method == 'POST':
            form = PatientForm(request.POST)
            if form.is_valid():
                patient = form.save()
                AuditLog.objects.create(
                    user=request.user,
                    action='CREATE',
                    model_name='Patient',
                    object_id=str(patient.id),
                    details=f"Created patient record for {patient.name}"
                )
                messages.success(request, 'Patient added successfully!')
                return redirect('patient_detail', pk=patient.pk)
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = PatientForm()
        return render(request, 'clinical/patient_form.html', {'form': form})
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('patient_list')

# Add similar views for Order and Task management...