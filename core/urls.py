from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'),
    # You can add more URL patterns here as you create more views
]