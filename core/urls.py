# core/urls.py

from django.urls import path
from . import views  # Import views to use the `home` function

urlpatterns = [
    path('', views.home, name='home'),  # Home view for the root URL
]

# hsis/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clinical/', include('clinical_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Include this line
    path('clinical/', include('clinical.urls')),  # Include your clinical app URLs
    path('', views.home, name='home'),  # Home view for the root URL
]