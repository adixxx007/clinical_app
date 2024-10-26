from django.urls import path, include
from . import views

urlpatterns = [
    path('clinicalnotes/', views.clinicalnote_list, name='clinicalnote_list'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patients/create/', views.patient_create, name='patient_create'),
    path('orders/', views.order_list, name='order_list'),
    path('clinical/', include('clinical.urls')),  # Corrected include
]
