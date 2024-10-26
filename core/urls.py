from django.urls import path
from . import views

urlpatterns = [
    path('clinicalnotes/', views.clinicalnote_list, name='clinicalnote_list'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/new/', views.patient_create, name='patient_create'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('orders/', views.order_list, name='order_list'),
    path('', views.clinical_home, name='clinical_home'),
    path('health/', views.health_check, name='health_check'),
]