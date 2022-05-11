from django.shortcuts import render

from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django_filters import rest_framework as filters_rest
from rest_framework import generics as api_views,permissions

from Cars.cars_rest.models import CarBrand, CarModel, UserCar
from Cars.cars_rest.serializers import InfoAllUsersSerializer, CarBrandSerializer, CarModelSerializer, \
    CreateCarSerializer, CarSerializer
from Cars.users_app.models import CustomCarUser

""" here users logic"""



class UserFilterSet(filters_rest.FilterSet):
    class Meta:
        model = CustomCarUser
        fields = ('id',)




class UsersListView(api_views.ListAPIView):
    """ show all users in the implemented html page"""
    permission_classes = (
        permissions.IsAuthenticated,
        permissions.BasePermission
    )
    serializer_class = InfoAllUsersSerializer
    filter_backends = [filters_rest.DjangoFilterBackend]
    filterset_class=UserFilterSet
    def get_queryset(self,**kwargs):
        query=''
        search_id = self.request.query_params.get('id', None)
        queryset=CustomCarUser.objects.all()
        if search_id:
            query=queryset.filter(id=search_id)
        else:
            query=queryset
        return query

""" here are the brands logic"""



class ListBrands(api_views.ListCreateAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

class SingleCarBrandView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


""" here are the models logic"""


class ListModels(api_views.ListCreateAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

class SingleCarModelView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


""" here are the car logic"""
class CarsFilterSet(filters_rest.FilterSet):
    class Meta:
        model = UserCar
        fields = ('user','car_brand','car_model','first_reg','odometer')




class CreateCarView(api_views.CreateAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = CreateCarSerializer



class ListCars(api_views.ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    queryset = UserCar.objects.all()
    serializer_class = CarSerializer
    filter_backends = [filters_rest.DjangoFilterBackend]
    filterset_class = CarsFilterSet
    


class SingleCarView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = UserCar.objects.all()
    serializer_class = CarSerializer






