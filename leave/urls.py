from django.urls import path
from . import views


urlpatterns=[
    path('leave/',views.leaverequest, name="add-request"),
    path('request-all/',views.request_table, name="table"),
   
]