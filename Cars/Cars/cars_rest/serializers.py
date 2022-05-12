from django.contrib.auth import get_user_model
from rest_framework import serializers

from Cars.cars_rest.models import CarBrand, CarModel, UserCar
from Cars.users_app.models import CustomCarUser

""" users serializers"""
class ListUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomCarUser
        fields = '__all__'
        #fields = ('username', 'first_name', 'last_name',"password")



class InfoAllUsersSerializer(serializers.ModelSerializer):
    """show the date from the db"""
    class Meta:
        model = CustomCarUser
        fields = '__all__'
        #fields = ('username', 'first_name', 'last_name')

class UpdateUsersSerializer(serializers.ModelSerializer):
    """show the date from the db"""
    class Meta:
        model = CustomCarUser
        fields = ('username','first_name','last_name')







""" car brands serializers """
class CarBrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarBrandSerializer(serializers.ModelSerializer):
    #name = OnlyNameCarBrandSerializer(many=True)

    class Meta:
        model = CarBrand
        fields = ('name',)


""" car models serializers """
class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'



""" cars serializers """
class UpdateCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields=('user','car_brand','car_model','first_reg','odometer')



class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields=('car_brand','car_model','first_reg','odometer')

class CreateCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = ('user','car_brand','car_model','first_reg','odometer')
