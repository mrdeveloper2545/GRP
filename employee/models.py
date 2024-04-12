from django.db import models
from django.contrib.auth.models import User,Group
from django.utils import timezone

# Create your models here.

class Employee(models.Model):
    employee=models.ForeignKey(User, on_delete=models.CASCADE)
    department=models.ForeignKey(Group, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    hire_date = models.DateField(default=timezone.now)


    def __str__(self):
        return self.employee.username
    
    
