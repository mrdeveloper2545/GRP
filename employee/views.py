from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import Group
from .forms import DepartmentForm,AddEmployeeForm,UserCreationForm


# add department
def add_department(request):
    form = DepartmentForm(request.POST or None)
    if request.method== "POST":
        if form.is_valid():
            department=form.cleaned_data['department']
            department = Group.objects.create(name=department)
            department.save()
            return redirect('department-table')
    return render(request, 'department.html', {'form':form})


# view alldepartment
def department_list(request):
    departments = Group.objects.all()
    return render(request, "department_all.html", {'departments':departments})    


# add employee

def add_employee(request):
   form=AddEmployeeForm()
   if request.method=="POST":
       form=AddEmployeeForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('login')
       else:
           form=AddEmployeeForm()
           return render(request, 'add-emp.html',{'form':form})
   return render(request, 'add-emp.html',{'form':form})
       