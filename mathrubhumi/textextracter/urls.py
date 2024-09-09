from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name='register_view'),
    path('home/', views.home_view, name='home'),
    path('failed/', views.home_view, name='failed'),
]