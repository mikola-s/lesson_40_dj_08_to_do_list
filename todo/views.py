from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, TemplateView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class Index(TemplateView):
    template_name = 'todo/index.html'


class CreateUser(CreateView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    success_url = '/'


class Login(LoginView):
    template_name = 'todo/login.html'
    success_url = '/'


class Logout(LogoutView):
    template_name = 'todo/logout.html'
    next_page = '/'
