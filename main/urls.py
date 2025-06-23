from django.urls import path
from . import views
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', lambda request: redirect('main', permanent=False)),
    path('main', views.main, name='main'),
    path('contacts', views.contacts, name='contacts'),
    path('t', views.tester, name='tester'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('conf/', views.conf, name='configuration'),
    path('msg', views.msg, name='msg'),
    path('register/', views.register_view, name='register'),
]