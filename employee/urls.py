from django.urls import path
from . import views

urlpatterns=[
#     department
       path('add-department/', views.add_department, name="department-form"),
       path('department-list/', views.department_list, name="department-table"),
       path('delete/<int:pk>/', views.delete_department, name="delete"),

       # salary
       path('add-salary/', views.add_salary, name="salary-form"),
       path('salary-table/', views.salary_table, name="salary-table"),



       # user
       path('add-user/',views.user_creation, name="user-form"),
       path('all-users/',views.all_user, name="user-list"),
    


       # employee
       path('add-emp/',views.add_employee, name="employee-form"), 
       path('delete-emp/<int:pk>',views.delete_employee, name="delete-emp"),
       path('emp-table/',views.emp_table, name="employee-table"),
       path('emp-record/<int:employee_id>',views.emp_record, name="record-emp"),
       path('emp-update/<int:pk>',views.update_emp, name="update"),
      
]