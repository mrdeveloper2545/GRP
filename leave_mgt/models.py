from django.db import models
from employee.models import Employee

# Create your models here.

class LeaveRequest(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    reason=models.TextField()
    status=models.CharField(max_length=20, default='pending')
