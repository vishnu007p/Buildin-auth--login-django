from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
    path('home/', views.home_view, name='home'),
    path('admin/', views.admin_view, name='admin'),
    path('loggedout/', views.loggedout_view, name='loggedout'),
    path('failed/', views.failed_view, name='failed'),
]