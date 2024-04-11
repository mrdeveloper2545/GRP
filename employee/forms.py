from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from  django import forms
from employee.models import Employee


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
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    department = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password', 'department',] 

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff=True
        user.set_password(self.cleaned_data["password"])
        if commit:    
            user.save()
            user.groups.add(self.cleaned_data['group'])
        return user    
        

class AddEmployeeForm(forms.ModelForm):
    employee=forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))     
    department=forms.ModelChoiceField(queryset=Group.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    hire_date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
      
      
    class Meta:
        model = Employee
        fields = ('employee','department', 'address','hire_date')
