from django.test import TestCase, Client
from django.urls import reverse
from .models import Patient, ClinicalNote

class PatientTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.patient = Patient.objects.create(
            name="Test Patient",
            age=30,
            address="Test Address",
            medical_history="Test History"
        )

    def test_patient_creation(self):
        self.assertEqual(self.patient.name, "Test Patient")
        self.assertEqual(self.patient.age, 30)

    def test_patient_list_view(self):
        response = self.client.get(reverse('patient_list'))
        self.assertEqual(response.status_code, 302)  # Should redirect to login