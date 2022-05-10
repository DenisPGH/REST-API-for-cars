from django.shortcuts import render

from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django_filters import rest_framework as filters_rest
from rest_framework import generics as api_views,permissions

from Cars.cars_rest.models import CarBrand, CarModel, UserCar
from Cars.users_app.models import CustomCarUser


class InfoAllUsersSerializer(serializers.ModelSerializer):
    """show the date from the db"""
    class Meta:
        model = CustomCarUser
        fields = '__all__'


class MyFilterSet(filters_rest.FilterSet):
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
    filterset_class=MyFilterSet
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
class OnlyNameCarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ( 'name',)


class CarBrandSerializer(serializers.ModelSerializer):
    #name = OnlyNameCarBrandSerializer(many=True)

    class Meta:
        model = CarBrand
        fields = ('name',)

class ListBrands(api_views.ListCreateAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


""" cars models"""

class OnlyNameCarModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ( 'name',)


class CarModelSerializer(serializers.ModelSerializer):
    #name = OnlyNameCarBrandSerializer(many=True)

    class Meta:
        model = CarModel
        fields = ('name',)

class ListModels(api_views.ListCreateAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


""" cars"""

class OnlyNameCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    #name = OnlyNameCarBrandSerializer(many=True)

    class Meta:
        model = UserCar
        fields = '__all__'

class ListCars(api_views.ListCreateAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    queryset = UserCar.objects.all()
    serializer_class = CarSerializer


class SingleCarView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = UserCar.objects.all()
    serializer_class = CarSerializer






