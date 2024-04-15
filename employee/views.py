from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import Group,User
from employee.models import Employee,salary
from .forms import DepartmentForm,AddEmployeeForm,UserCreationForm,SalaryForm
from django.contrib.auth.decorators import login_required


#  department
@login_required
def add_department(request):
    form = DepartmentForm(request.POST or None)
    if request.method== "POST":
        if form.is_valid():
            department=form.cleaned_data['department']
            department = Group.objects.create(name=department)
            department.save()
            return redirect('department-table')
    return render(request, 'department.html', {'form':form})


def department_list(request):
    departments = Group.objects.all()
    
    # Number of items per page
    items_per_page = 10
    
    paginator = Paginator(departments, items_per_page)
    
    page_number = request.GET.get('page')
    
    try:
        departments = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        departments = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        departments = paginator.page(paginator.num_pages)
    
    return render(request, "department_all.html", {'departments': departments})


# salary
@login_required
def add_salary(request):
    form = SalaryForm(request.POST or None)
    if request.method== "POST":
        if form.is_valid():
            form.save()
            return redirect('salary-table')
    return render(request, 'salary.html', {'form':form})


def salary_table(request):
    salary_list=salary.objects.all()

    items_per_page = 10

    paginator =Paginator(salary_list, items_per_page)

    page_number=request.GET.get('page')

    try:
        salary_list = paginator.page(page_number)
    except PageNotAnInteger:     
        salary_list=paginator.page(1)

    except EmptyPage:
        salary_list=paginator.page(paginator.num_pages)
    return render(request, 'salary-table.html',{'salary_list':salary_list})

# create usre(staff)
def user_creation(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee-table')
        else:
            form=UserCreationForm()
            return render(request, 'add-user.html',{'form':form})
    return render(request, 'add-user.html', {'form':form})

# add employee
@login_required
def add_employee(request, pk):
    current_user = get_object_or_404(User, id=pk)
    user_form = UserCreationForm(request.POST or None, instance=current_user)
    employee_form = AddEmployeeForm(request.POST or None)
    if request.method == "POST":
        if user_form.is_valid() and employee_form.is_valid():
            user_form.save()
            employee_form.save()
            return redirect('employee-table')
        else:
            user_form = UserCreationForm(instance=current_user)
            employee_form = AddEmployeeForm()
        return render(request, 'add-emp.html',{'user_form':user_form, 'employee_form':employee_form})
    return render(request, 'add-emp.html',{'user_form':user_form, 'employee_form':employee_form})


# view all employee
@login_required
def emp_table(request):
    employees = Employee.objects.all()

    items_per_page = 10

    paginator = Paginator(employees, items_per_page)

    page_number = request.GET.get('page')

    try:
        employees=paginator.page(page_number)

    except PageNotAnInteger:

        employees=paginator.page(1)

    except EmptyPage:

        employees = paginator.page(paginator.num_pages)

    return render(request,'emp-table.html',{'employees':employees})


# view all registered user
@login_required
def all_user(request):
    users=User.objects.all()

    items_per_page = 10

    paginator = Paginator(users, items_per_page)

    page_number = request.GET.get('page')

    try:
        users=paginator.page(page_number)

    except PageNotAnInteger:

        users=paginator.page(1)

    except EmptyPage:

        users=paginator.page(paginator.num_pages)
    return render(request, 'user-table.html','profile.html',{'users':users})

# delete employee
@login_required
def delete_employee(request, pk):
    delete=User.objects.get(id=pk)
    delete.delete()
    return redirect('employee-table')


def emp_record(request, employee_id):
    employee=Employee.objects.get(id=employee_id)
    return render(request, 'emp-record.html', {'employee':employee})


