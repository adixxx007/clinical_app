from django.test import TestCase, Client
from django.urls import reverse
from .models import Patient, ClinicalNote

class PatientTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.patient = Patient.objects.create(
            name="Test Patient",
            patient_id="P12345",
            age=30,
            address="Test Address",
            medical_history="Test History"
        )

    def test_patient_creation(self):
        self.assertEqual(self.patient.name, "Test Patient")
        self.assertEqual(self.patient.age, 30)
        self.assertEqual(self.patient.patient_id, "P12345")

    def test_patient_list_view(self):
        response = self.client.get(reverse('patient_list'))
        self.assertEqual(response.status_code, 302)  # Should redirect to login
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('patient_list')}")

class ClinicalNoteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.patient = Patient.objects.create(
            name="Test Patient",
            patient_id="P12345",
            age=30,
            address="Test Address",
            medical_history="Test History"
        )
        self.note = ClinicalNote.objects.create(
            patient=self.patient,
            note="Test Note",
            diagnosis="Test Diagnosis",
            treatment_plan="Test Treatment Plan",
            created_by=None  # Assuming no user is associated for simplicity
        )

    def test_clinical_note_creation(self):
        self.assertEqual(self.note.note, "Test Note")
        self.assertEqual(self.note.diagnosis, "Test Diagnosis")
        self.assertEqual(self.note.treatment_plan, "Test Treatment Plan")
        self.assertEqual(self.note.patient.name, "Test Patient")