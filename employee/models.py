from django.db import models
from django.contrib.auth.models import User,Group
from django.utils import timezone
import uuid

# Create your models here.
class salary(models.Model):
    department=models.OneToOneField(Group, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "salaries"
        unique_together = ['department']

    def __str__(self):
        return f"{self.department.name} - ${self.amount}"  
    


    
class Employee(models.Model):
    employee=models.OneToOneField(User, on_delete=models.CASCADE)
    department=models.OneToOneField(Group, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    hire_date = models.DateField(default=timezone.now)
    
    
 


    def __str__(self):
        return self.employee.username
    
        
    
    
