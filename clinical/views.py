from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from django.contrib.auth.decorators import login_required

@login_required
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'clinical/patient_form.html', {'form': form})
from django.shortcuts import render, get_object_or_404
from .models import Patient
from django.contrib.auth.decorators import login_required

@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'clinical/patient_list.html', {'patients': patients})

@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'clinical/patient_detail.html', {'patient': patient})

from .forms import PatientForm