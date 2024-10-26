from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from clinical_app.clinical.forms import ClinicalNoteForm
from clinical_app.core.models import Patient

def home(request):
    return HttpResponse("Hello, world! This is the home page.")

def add_clinical_note(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = ClinicalNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.patient = patient
            note.save()
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = ClinicalNoteForm()
    return render(request, 'clinical/add_clinical_note.html', {'form': form})