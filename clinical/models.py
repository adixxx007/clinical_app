from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    medical_record_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class ClinicalNote(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    note_type = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"Note for {self.patient} by {self.author}"

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