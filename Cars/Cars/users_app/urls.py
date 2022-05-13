from django.urls import path

from Cars.users_app.views import MyLoginView, RegistrationView, MainPageView, LogoutPageView

urlpatterns=(
    path('', MyLoginView.as_view(), name='loginJ'),
    path('registration/',RegistrationView.as_view(),name='registration'),
    path('login/', MainPageView.as_view(), name='main'),
    path('logout/',LogoutPageView.as_view(),name='logout'),
)