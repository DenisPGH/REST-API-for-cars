from django.urls import path

from Cars.cars_rest.views import UsersListView, ListBrands, ListModels, ListCars, SingleCarView

urlpatterns=(
    path('user/',UsersListView.as_view(),name="restusers"),
    path('brands/',ListBrands.as_view(),name="brands"),
    path('models/',ListModels.as_view(),name="models"),
    path('car/',ListCars.as_view(),name="cars"),
    path('car/<int:pk>/', SingleCarView.as_view(), name='single car'),

)
