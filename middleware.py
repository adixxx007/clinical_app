from django.utils import timezone
from .models import AuditLog

class AuditLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated and request.method in ['POST', 'PUT', 'DELETE']:
            AuditLog.objects.create(
                user=request.user,
                action=request.method,
                model_name=request.path.split('/')[-2],
                object_id=request.path.split('/')[-1],
                details=f"Access to {request.path}"
            )

        return response