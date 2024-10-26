from django import forms
from .models import Patient, ClinicalNote, Order, Task
from django.contrib.auth.models import User

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'patient_id', 'age', 'address', 'medical_history']
        widgets = {
            'medical_history': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 0:
            raise forms.ValidationError("Age cannot be negative")
        return age

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
        fields = ['order_type', 'description', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['assigned_to', 'description', 'due_date', 'priority', 'related_patient']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class PatientSearchForm(forms.Form):
    search_query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search patients...'})
    )
    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )