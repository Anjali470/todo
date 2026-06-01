from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from .models import ToDo

def login(request):
    return render(request, 'login.html')