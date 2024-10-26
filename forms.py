from django import forms
from .models import ClinicalNote, Order, Patient

class ClinicalNoteForm(forms.ModelForm):
    class Meta:
        model = ClinicalNote
        fields = ['note', 'diagnosis', 'treatment_plan', 'next_appointment']
        widgets = {
            'next_appointment': forms.DateInput(attrs={'type': 'date'}),
            'treatment_plan': forms.Textarea(attrs={'rows': 4}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['description', 'order_type', 'notes']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'medical_history']