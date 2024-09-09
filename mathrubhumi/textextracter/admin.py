from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('email','employee_number', 'is_staff')
    search_fields = ('email','employee_number')
    ordering = ('email',)

    filter_horizontal = []
    list_filter=()
    fieldsets=()

admin.site.register(CustomUser, CustomUserAdmin)
