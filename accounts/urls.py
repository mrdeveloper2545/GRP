from django.urls import path
from . import views



urlpatterns = [
    path('', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('dashbord', views.dashbord, name="dashboard"),
    path('change-password/', views.change_password, name='change_password'),
]