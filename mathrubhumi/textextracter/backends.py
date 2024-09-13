from django.contrib.auth.backends import BaseBackend
from .models import CustomUser

class EmployeeBackend(BaseBackend):
    def authenticate(self, request, employee_number=None, password=None):
        try:
            user = CustomUser.objects.get(employee_number=employee_number)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
