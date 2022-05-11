from django.urls import path

from Cars.cars_rest.views import UsersListView, ListBrands, ListModels, ListCars, SingleCarView, SingleCarModelView, \
    SingleCarBrandView, CreateCarView, UserViewSet, BrandsViewSet

urlpatterns=(
    path('user/',UsersListView.as_view(),name="restusers"),
    #path('user/',UserViewSet.as_view({'get': 'list'}),name="restusers"),
    #path('brand/',ListBrands.as_view(),name="brands"),
    path('brand/',BrandsViewSet.as_view({'get': 'list'}),name="brands"),
    path('brand/<int:pk>/', BrandsViewSet.as_view({'get': 'retrieve'}), name='single brand'),
    path('model/',ListModels.as_view(),name="models"),
    path('model/<int:pk>/', SingleCarModelView.as_view(), name='single model'),
    path('car/',ListCars.as_view(),name="cars"),
    path('car/<int:pk>/', SingleCarView.as_view(), name='single car'),
    path('create_car/', CreateCarView.as_view(), name='create car'),

)
