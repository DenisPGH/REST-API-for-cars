from django.urls import path

from Cars.users_app.views import LoginView, RegistrationView

urlpatterns=(
    path('',LoginView.as_view(),name='login'),
    path('regi/',RegistrationView.as_view(),name='registration'),
)