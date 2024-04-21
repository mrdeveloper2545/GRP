from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from  django import forms
from employee.models import Employee,salary


class DepartmentForm(forms.Form):
    department=forms.CharField(label="department",max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_department(self):
        department=self.cleaned_data['department']
        if Group.objects.filter(name=department).exists():
            raise forms.ValidationError("department with that name already exist")
        return department
    


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

  
    
   
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password',] 


    def save(self, commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_staff=True
        if commit:
            user.save()
        return user.username    

class AddEmployeeForm(forms.ModelForm):
    employee=forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))     
    department=forms.ModelChoiceField(queryset=Group.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    hire_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    
    
    
      
      
    class Meta:
        model = Employee
        fields = ('employee','department', 'address','hire_date',)

  
    def save(self, commit=True):
        employee=super().save(commit=False)
        if commit:
            employee.save()
            employee.employee.groups.add(self.cleaned_data['department'])
        return employee.employee.username



class SalaryForm(forms.ModelForm):
    department=forms.ModelChoiceField(queryset=Group.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    amount=forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = salary
        verbose_name_plural = "Salaries"
        fields = ['department', 'amount']



        


    



