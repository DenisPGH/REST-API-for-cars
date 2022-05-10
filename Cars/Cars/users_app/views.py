from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
# Create your views here.
from Cars.users_app.models import CustomCarUser
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import mixins as auth_mixin
from django.contrib.auth import forms as auth_forms


class MyLoginView(LoginView,auth_mixin.LoginRequiredMixin):
    template_name = 'index.html'
    def get_success_url(self):
        return reverse_lazy('main')

class LogoutPageView(LogoutView):
    """ by pressing logout, redirect to fitst page"""
    def get_success_url(self):
        return reverse_lazy('index')

class CreateNewUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = CustomCarUser
        fields = ('username','first_name', 'last_name','password1', 'password2', )


class RegistrationView(views.CreateView):
    form_class = CreateNewUserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('loginJ')


class RestTest(views.TemplateView,auth_mixin.LoginRequiredMixin):
    template_name = 'login.html'