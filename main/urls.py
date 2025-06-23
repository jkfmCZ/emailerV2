from django.urls import path
from . import views
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', lambda request: redirect('main', permanent=False)),
    path('main', views.main, name='main'),
    path('contacts', views.contacts, name='contacts'),
    path('t', views.tester, name='tester'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', csrf_exempt(LogoutView.as_view()), name='logout'),
    path('conf/', views.conf, name='configuration'),
    path('msg', views.msg, name='msg'),
    path('register/', views.register_view, name='register'),
]