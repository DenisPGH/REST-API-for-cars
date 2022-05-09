from django.shortcuts import render
from django.views import generic as views
# Create your views here.

class LoginView(views.TemplateView):
    template_name = 'index.html'



class RegistrationView(views.TemplateView):
    template_name = 'registration.html'
