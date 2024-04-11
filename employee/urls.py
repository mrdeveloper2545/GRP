from django.urls import path
from . import views

urlpatterns=[
       path('add-department/', views.add_department, name="department-form"),
       path('department-list/', views.department_list, name="department-table"),
       path('add-emp',views.add_employee, name="employee-form"),
]