from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import ClinicalNote, Patient, Order  # Assuming Order and Patient models exist
from .forms import ClinicalNoteForm, PatientForm, OrderForm


# View for listing clinical notes
@login_required
def clinicalnote_list(request):
    notes = ClinicalNote.objects.all()
    return render(request, 'core/clinicalnote_list.html', {'notes': notes})

# View for listing patients
@login_required
def patient_list(request):
    patients = Patient.objects.all().order_by('-created_at')
    paginator = Paginator(patients, 10)  # Show 10 patients per page
    page_number = request.GET.get('page')
    patients = paginator.get_page(page_number)
    return render(request, 'core/patient_list.html', {'patients': patients})

# View for patient detail
@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    notes = ClinicalNote.objects.filter(patient=patient)  # Assuming ClinicalNote has a ForeignKey to Patient
    return render(request, 'core/patient_detail.html', {'patient': patient, 'notes': notes})

# View for creating a new patient
@login_required
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient added successfully.")
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'core/patient_form.html', {'form': form})

# View for listing orders
@login_required
def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    paginator = Paginator(orders, 10)  # Show 10 orders per page
    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)
    return render(request, 'core/order_list.html', {'orders': orders})

# View for clinical home page (assuming this exists)
@login_required
def clinical_home(request):
    return render(request, 'core/clinical_home.html')
