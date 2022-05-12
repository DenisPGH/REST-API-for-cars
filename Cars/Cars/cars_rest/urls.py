from django.urls import path

from Cars.cars_rest.views import UsersListView, ListModels, ListCars, SingleCarModelView, \
     BrandsViewSet, UserViewSet, SingleCarViewSet, SingleBrandViewSet

urlpatterns=(
    path('user/',UsersListView.as_view(),name="restusers"),
    path('user/<int:pk>/',UserViewSet.as_view({'get':'show','put':'put','delete':'destroy'}),name="edit user"),
    path('brand/',BrandsViewSet.as_view({'get': 'list','put':'create'}),name="brands"),
    path('brand/<int:pk>/', SingleBrandViewSet.as_view({'get': 'show','put':'put','delete':'destroy'}), name='single brand'),
    path('model/',ListModels.as_view(),name="models"),
    path('model/<int:pk>/', SingleCarModelView.as_view(), name='single model'),
    path('car/',ListCars.as_view(),name="cars"),
    path('car/<int:pk>/', SingleCarViewSet.as_view({'get': 'show', 'put': 'put', 'delete': 'destroy'}), name='single car'),


)
