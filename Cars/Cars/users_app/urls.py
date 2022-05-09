from django.urls import path

from Cars.users_app.views import MyLoginView, RegistrationView, RestTest

urlpatterns=(
    path('', MyLoginView.as_view(), name='loginJ'),
    path('regi/',RegistrationView.as_view(),name='registration'),
    path('log/',RestTest.as_view(),name='main'),
)