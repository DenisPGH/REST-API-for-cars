from django.urls import path

from Cars_root.Cars.cars_rest.views import UsersListView, ListModels, ListCars, SingleCarModelView, \
     BrandsViewSet, UserViewSet, SingleCarViewSet, SingleBrandViewSet

urlpatterns=(
    path('users/',UsersListView.as_view(),name="restusers"),
    path('users/<int:pk>/',UserViewSet.as_view({'get':'show','put':'put','delete':'destroy'}),name="edit user"),
    path('brands/',BrandsViewSet.as_view({'get': 'list','post':'create'}),name="brands"),
    path('brands/<int:pk>/', SingleBrandViewSet.as_view({'get': 'show','put':'put','delete':'destroy'}), name='single brand'),
    path('models/',ListModels.as_view(),name="models"),
    path('models/<int:pk>/', SingleCarModelView.as_view(), name='single model'),
    path('cars/',ListCars.as_view(),name="cars"),
    path('cars/<int:pk>/', SingleCarViewSet.as_view({'get': 'show', 'put': 'put', 'delete': 'destroy'}), name='single car'),


)
