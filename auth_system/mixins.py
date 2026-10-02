from .models import CustomUser
from django.shortcuts import redirect
class AdminRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_admin_role():
            return redirect('login')  # Redirect to login page if user is not authenticated or not an admin
        return super().dispatch(request, *args, **kwargs)
