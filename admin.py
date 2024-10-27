from django.contrib import admin
from .models import Patient, ClinicalNote, Order, Task, AuditLog

admin.site.register(Patient)
admin.site.register(ClinicalNote)
admin.site.register(Order)
admin.site.register(Task)
admin.site.register(AuditLog)