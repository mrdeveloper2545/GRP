from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class GroupPassword(models.Model):
    department=models.ForeignKey(Group, on_delete=models.CASCADE)
    department_password=models.CharField(max_length=128)   

def authenticate_user(username, password):
    try:
        user=User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    
    departments=user.department.all()
    for department in departments:
        try:
            department_password=GroupPassword.objects.get(department=department)
            if department_password.department== password:
                return user
        except GroupPassword.DoesNotExist:
            return None   
 

