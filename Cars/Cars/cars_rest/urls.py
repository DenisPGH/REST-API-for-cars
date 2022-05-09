from django.urls import path

from Cars.cars_rest.views import UsersListView

urlpatterns=(
    path('rest/',UsersListView.as_view(),name="restusers"),

)
