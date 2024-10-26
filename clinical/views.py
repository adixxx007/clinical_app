# clinical/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patient, ClinicalNote, Order  # Import the Order model to use in the order_list view
from .forms import PatientForm

# ======================
# Patient Views
# ======================

@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'clinical/patient_list.html', {'patients': patients})

@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'clinical/patient_detail.html', {'patient': patient})


@login_required
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient added successfully!')
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'clinical/patient_form.html', {'form': form})

# ======================
# Clinical Note Views
# ======================

@login_required
def clinicalnote_list(request):
    notes = ClinicalNote.objects.all()
    return render(request, 'clinical/clinicalnote_list.html', {'notes': notes})

# ======================
# Order Views
# ======================

@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'clinical/order_list.html', {'orders': orders})
