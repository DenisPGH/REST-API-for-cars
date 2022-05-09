from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
# Create your views here.
from Cars.users_app.models import CustomCarUser
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import mixins as auth_mixin


class MyLoginView(LoginView):
    template_name = 'index.html'
    def get_success_url(self):
        return reverse_lazy('restusers')

class LogoutPageView(LogoutView):
    """ by pressing logout, redirect to fitst page"""
    def get_success_url(self):
        return reverse_lazy('index')



class RegistrationView(views.CreateView):
    model=CustomCarUser
    fields = ('password','username','first_name','last_name')
    template_name = 'registration.html'
    success_url = reverse_lazy('loginJ')


class RestTest(views.TemplateView,auth_mixin.LoginRequiredMixin):
    template_name = 'login.html'