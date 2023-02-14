from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.LoginUser, name='loginUser'),
    path(r'projects/curriculum-vitae/register', views.RegisterUser, name='registerUser'),


]