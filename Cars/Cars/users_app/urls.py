from django.urls import path

from Cars.users_app.views import MyLoginView, RegistrationView, MainPageView, LogoutPageView

urlpatterns=(
    path('', MyLoginView.as_view(), name='loginJ'),
    path('regi/',RegistrationView.as_view(),name='registration'),
    path('log/', MainPageView.as_view(), name='main'),
    path('logout/',LogoutPageView.as_view(),name='logout'),
)