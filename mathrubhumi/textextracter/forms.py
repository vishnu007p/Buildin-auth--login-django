from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email','employee_number','password']

        def __init__(self, *args, **kwargs):
            super(CustomUserCreationForm, self).__init__(*args, **kwargs)
            self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
            self.fields['employee_number'].widget.attrs['placeholder'] = 'Employee Number'
            self.fields['password'].widget.attrs['placeholder'] = 'Enter Password'
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'input'

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'employee_number','is_active','is_staff','is_superadmin',)