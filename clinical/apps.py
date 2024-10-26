from django.apps import AppConfig


class ClinicalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clinical'  # This should match your app directory name ('clinical')
