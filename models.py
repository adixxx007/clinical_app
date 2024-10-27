from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    medical_history = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ClinicalNote(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note = models.TextField()
    next_appointment = models.DateTimeField(null=True, blank=True)
    diagnosis = models.TextField(blank=True)
    treatment_plan = models.TextField(blank=True)

    def __str__(self):
        return f"Note for {self.patient.first_name} {self.patient.last_name}"

class Order(models.Model):
    description = models.TextField()
    order_type = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add for created_at
    updated_at = models.DateTimeField(auto_now=True)  # auto_now for updated_at

    def __str__(self):
        return self.description

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)  # Default value for completed
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add for created_at
    updated_at = models.DateTimeField(auto_now=True)  # auto_now for updated_at

    def __str__(self):
        return self.title

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # ForeignKey to User, allows null
    action = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    object_id = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)  # auto_now_add for timestamp
    details = models.TextField()

    def __str__(self):
        return f"{self.action} by {self.user} at {self.timestamp}"