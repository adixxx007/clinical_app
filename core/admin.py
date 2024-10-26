from django.contrib import admin
from .models import Patient, ClinicalNote, Order

admin.site.register(Patient)
admin.site.register(ClinicalNote)
admin.site.register(Order)
