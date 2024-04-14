from django.shortcuts import render,redirect
from .forms import LeaveCreationForm
from .models import Leave
from django.contrib.auth.decorators import login_required

# Create your views here.

# create leave
@login_required
def create_leave(request):
    form=LeaveCreationForm(request.POST)
    if request.method== "POST":
       if form.is_valid():
           instance=form.save(commit=False)
           employee=instance.employee
           instance.employee=employee
           instance.save()
       else:
           form=LeaveCreationForm()
    return render(request, 'leave-create.html',{'form':form})