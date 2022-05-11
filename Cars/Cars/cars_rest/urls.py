from django.urls import path

from Cars.cars_rest.views import UsersListView, ListModels, ListCars, SingleCarView, SingleCarModelView, \
    CreateCarView, BrandsViewSet, UserViewSet

urlpatterns=(
    path('user/',UsersListView.as_view(),name="restusers"),
    path('user/<int:pk>/',UserViewSet.as_view({'get':'update'}),name="edit user"),
    path('brand/',BrandsViewSet.as_view({'get': 'list'}),name="brands"),
    path('brand/<int:pk>/', BrandsViewSet.as_view({'get': 'update'}), name='single brand'),
    path('model/',ListModels.as_view(),name="models"),
    path('model/<int:pk>/', SingleCarModelView.as_view(), name='single model'),
    path('car/',ListCars.as_view(),name="cars"),
    path('car/<int:pk>/', SingleCarView.as_view(), name='single car'),
    path('create_car/', CreateCarView.as_view(), name='create car'),

)
