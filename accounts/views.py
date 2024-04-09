from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User






# LOGIN USER
def login_user(request):
    if request.method== 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           return redirect('group')
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})
        


# logout
def logout_user(request):
    logout(request)
    return redirect('home')









        
        