from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import ToDo

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('todo.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['confirm_password']
        email = request.POST['email']
        if password1 == password:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error': 'Username already exists'})
            elif User.objects.filter(email=email).exists():
                return render(request, 'register.html', {'error': 'Email already exists'})
            else:
                 user = User.objects.create_user(username=username, password=password, email=email)
                 user.save()
                 return redirect('login')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'register.html')