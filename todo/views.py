from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, TemplateView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class Index(TemplateView):
    template_name = 'todo/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateUser(CreateView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        data = super().form_valid(form)
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return data


class Login(LoginView):
    template_name = 'todo/login.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    # def form_valid(self, form):
    #     login(self.request, form.get_user())
    #     return super().form_valid(form)


class Logout(LogoutView):
    template_name = 'todo/logout.html'
    next_page = '/'
