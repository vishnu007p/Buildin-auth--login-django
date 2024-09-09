from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site

from .models import CustomUser
from .forms import CustomUserCreationForm


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        print('inside')
        print('form valid', request.POST['email'])
        email = request.POST['email']
        employee_number = request.POST['employee_number']
        password = request.POST['password']

        user = CustomUser.objects.create_user(email=email, employee_number=employee_number, password=password)
        user.save()

        print('savedd')

        return redirect('home')
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
        
def home_view(request):
    return render(request, 'home.html')

def failed_view(request):
    return render(request, 'failed.html')
