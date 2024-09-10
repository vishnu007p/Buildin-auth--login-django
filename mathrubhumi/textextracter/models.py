from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email,employee_number, password=None):
        if not email:
            raise ValueError("The email field is required.")
        
        user=self.model(
            email=self.normalize_email(email),
            employee_number=employee_number
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,employee_number, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            employee_number = employee_number,
            password = password,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        
        return user
    

class CustomUser(AbstractBaseUser):
    email = models.CharField(max_length=100,unique=True)
    employee_number=models.CharField(max_length=15,unique=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    objects= CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['employee_number']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj = None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True


