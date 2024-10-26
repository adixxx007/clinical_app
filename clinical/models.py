from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    medical_history = models.TextField()

    def __str__(self):
        return self.name

class ClinicalNote(models.Model):
    patient = models.ForeignKey(Patient, related_name='notes', on_delete=models.CASCADE)
    note = models.TextField()  # Make sure this is defined correctly
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.patient.name} on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    
class Order(models.Model):
    ORDER_TYPES = [
        ('Lab', 'Lab Test'),
        ('Imaging', 'Imaging'),
        ('Medication', 'Medication'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=20, choices=ORDER_TYPES)
    description = models.CharField(max_length=255)
    date_ordered = models.DateTimeField(auto_now_add=True)
    ordered_by = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.order_type} Order for {self.patient}"

class Task(models.Model):
    assigned_to = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Task for {self.assigned_to}"