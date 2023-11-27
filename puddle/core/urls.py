from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginFrom

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.singup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html' ,authentication_form=LoginFrom), name='login'),
    path('logout/', views.logout_view, name='logout')
]