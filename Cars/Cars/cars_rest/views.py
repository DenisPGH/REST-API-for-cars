from django.shortcuts import render

from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django_filters import rest_framework as filters_rest
from rest_framework import generics as api_views,permissions
from django.shortcuts import get_object_or_404

from Cars.cars_rest.models import CarBrand, CarModel, UserCar
from Cars.cars_rest.serializers import InfoAllUsersSerializer, CarBrandSerializer, CarModelSerializer, \
    CreateCarSerializer, CarSerializer, CarBrandListSerializer, UpdateUsersSerializer, ListUsersSerializer
from Cars.users_app.models import CustomCarUser

""" here users logic"""
class UserFilterSet(filters_rest.FilterSet):
    class Meta:
        model = CustomCarUser
        fields = ('id',)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticated,
        permissions.BasePermission
    )
    queryset = CustomCarUser.objects.all()
    serializer_class = UpdateUsersSerializer
    # filter_backends = [filters_rest.DjangoFilterBackend]
    # filterset_class = UserFilterSet
    def show(self, request,pk=None, *args, **kwargs):
        user = CustomCarUser.objects.get(pk=pk)
        serializer = UpdateUsersSerializer(user)
        return Response(serializer.data)


    def put(self, request, pk=None):
        user = CustomCarUser.objects.get(pk=pk)
        data = request.data
        user.username=data['username']
        user.first_name=data['first_name']
        user.last_name=data['last_name']
        user.save()
        serializer = UpdateUsersSerializer(user)
        return Response(serializer.data)

    # def get_queryset(self,*args,**kwargs):
    #     # query=''
    #     # search_id = self.request.query_params.get('id', None)
    #     queryset=CustomCarUser.objects.all()
    #     # if search_id:
    #     #     query=queryset.filter(id=search_id)
    #     # else:
    #     #     query=queryset
    #     serializers=InfoAllUsersSerializer(queryset)
    #     return Response(serializers.data)

    def list(self, request, *args, **kwargs):
        queryset = CustomCarUser.objects.all()

        serializers_ = ListUsersSerializer(queryset)
        return Response(serializers_.data)















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
class BrandsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = CarBrand.objects.all()
        serializer = CarBrandListSerializer(queryset, many=True)
        return Response(serializer.data)


    def update(self, request, pk=None):
        brand = CarBrand.objects.get(pk=pk)
        serializer = CarBrandSerializer(brand)
        return Response(serializer.data)



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





