from django.urls import path
from . import views


urlpatterns=[
    path('leave/',views.leaverequest, name="add-request"),
    path('request-all/',views.request_table, name="table"),
    path('approve/<int:pk>/', views.approve_leave, name="approve"),
   

   
]