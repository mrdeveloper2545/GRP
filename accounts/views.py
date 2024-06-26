from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from employee.models import Employee
from django.contrib.auth.forms import PasswordChangeForm
from leave.models import LeaveRequest




# LOGIN USER
def login_user(request):
    if request.method== 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           messages.error(request, 'please provide the credential inforamation')
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
    total_user=User.objects.count()
    total_department=Group.objects.count()
    total_employees=Employee.objects.count()
    total_leaves=LeaveRequest.objects.count()
    return render(request,'homepage.html', {'total_employees':total_employees, 'total_user':total_user,'total_department':total_department,'total_leaves':total_leaves})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully change password now you can log in with your new password')  # Important to update the session with the new password hash
            return redirect('login') 
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})






  











        
        