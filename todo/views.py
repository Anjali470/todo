from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
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
            return redirect('todo')
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

@login_required(login_url='login')  
def todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        print(title)
        task = ToDo.objects.create(user=request.user, title=title)
        task.save()
        tasks = ToDo.objects.filter(user=request.user).order_by('-date')
        return redirect('/todo/', {'tasks': tasks})
    tasks = ToDo.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'tasks': tasks})
def logout(request):
    auth_logout(request)
    return redirect('login')