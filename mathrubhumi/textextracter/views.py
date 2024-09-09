from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import auth, messages
from django.contrib.sites.shortcuts import get_current_site

from .models import CustomUser
from .forms import CustomUserCreationForm

def admin_view(request):
    return render(request, 'admin.html')

def home_view(request):
    return render(request, 'home.html')

def failed_view(request):
    return render(request, 'failed.html')

def register_view(request):
    if request.method == 'POST':
        print('inside')
        print('form valid', request.POST['email'])
        email = request.POST['email']
        employee_number = request.POST['employee_number']
        password = request.POST['password']

        try:
            user = CustomUser.objects.create_user(email=email, employee_number=employee_number, password=password)
            user.save()
            print('savedd')
            return redirect('login')
        except IntegrityError as e:
            if 'email' in str(e):
                messages.error(request, 'Email already exists. Try logging in.')
            elif 'employee_number' in str(e):
                messages.error(request, 'Employee number already exists. Please contact support or try again.')
            print('duplicate email')
            return render(request,'register.html')

        # #form = CustomUserCreationForm(request.POST)
        # if form.is_valid():
        #     print('form valid', request.data)
            

        #     print('uswer saved')

        #     #current_site= get_current_site(request)

        #     messages.success(request,"Successfully registered. ")
        #     return redirect('home')
        # else:
        #     messages.error(request,"registration failed.")
        #     form = CustomUserCreationForm()
        #     return render(request,'register.html',{'form': form})
    #form = CustomUserCreationForm()
    return render(request,'register.html')
        
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        try:
            employee_number=request.POST.get('email')
            password = request.POST.get('password')
            
            user = auth.authenticate(employee_number=employee_number,password=password)
            print('inside')
            if user is not None:
                print('inside none')
                auth.login(request, user)
                if user.is_admin:
                    return redirect('admin')
                return redirect('home')
            else:
                messages.error(request, 'Credentials does not match. ')
                return redirect('login')
        except KeyError:
            messages.error(request,"Fields missing. ")
            return redirect('login')
    return render(request,'login.html')

