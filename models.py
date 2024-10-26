from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Patient(models.Model):
    name = models.CharField(max_length=100)
    patient_id = models.CharField(max_length=20, unique=True)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    address = models.TextField()
    medical_history = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['patient_id']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.name} ({self.patient_id})"

class ClinicalNote(models.Model):
    note = models.TextField()
    diagnosis = models.CharField(max_length=255)
    treatment_plan = models.TextField()
    next_appointment = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.note

class Order(models.Model):
    description = models.TextField()
    order_type = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('URGENT', 'Urgent')
    ]

    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MEDIUM')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    related_patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Task for {self.assigned_to.username} - {self.priority}"

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    object_id = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return f"{self.action} by {self.user} at {self.timestamp}"
    def __str__(self):
        return f"{self.action} by {self.user} at {self.timestamp}"
    
    