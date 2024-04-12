from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# LOGIN USER
def login_user(request):
    if request.method== 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           return redirect('dashboard')
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})
        
# LOGOUT USER
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def dashbord(request):
    return render(request,'homepage.html', {})









        
        