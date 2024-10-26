from django.db import models
from django.contrib.auth.models import User  # Importing User model


# Create your models here.

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class StaffMember(models.Model):
    ROLE_CHOICES = [
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
        ('Admin', 'Administrator'),
    ]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    schedule = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.CharField(max_length=200)
    is_emergency = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment on {self.date} for {self.patient}"
    
class ClinicalNote(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Indented function as part of the class
    def my_function(self):
        print("This is a properly indented block.")

from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=100)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
