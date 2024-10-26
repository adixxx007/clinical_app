from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('clinical/', include('clinical.urls')),
    path('', include('core.urls')),  # Home page and other core URLs
]

from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('patients/<int:pk>/add_note/', views.add_clinical_note, name='add_clinical_note'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

