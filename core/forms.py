# forms.py

from django import forms
from .models import Patient, ClinicalNote, Order

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'  # Or list specific fields

class ClinicalNoteForm(forms.ModelForm):
    class Meta:
        model = ClinicalNote
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
