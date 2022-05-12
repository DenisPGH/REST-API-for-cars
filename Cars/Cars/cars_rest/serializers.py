
from rest_framework import serializers
from Cars.cars_rest.models import CarBrand, CarModel, UserCar
from Cars.users_app.models import CustomCarUser




""" users serializers"""

class InfoAllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomCarUser
        fields = '__all__'


class UpdateUsersSerializer(serializers.ModelSerializer):
    """show the date from the db"""
    class Meta:
        model = CustomCarUser
        fields = ('username','first_name','last_name','hometown','picture','data_birth')







""" car brands serializers """
class CarBrandListSerializer(serializers.ModelSerializer):
    """serializer for create and list all brands"""
    def create(self, validated_data):
        new_brand = CarBrand.objects.create(
            name=validated_data['name'],
        )
        return new_brand
    
    class Meta:
        model = CarBrand
        fields = ('name',)


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ('name',)


""" car models serializers """
class CarModelSerializer(serializers.ModelSerializer):
    car_brand = serializers.CharField(source='car_brand.name')
    class Meta:
        model = CarModel
        fields = '__all__'

class UpdateCarModelSerializer(serializers.ModelSerializer):
    car_brand = serializers.CharField(source='car_brand.name')
    class Meta:
        model = CarModel
        fields = ('id','name','car_brand')



""" cars serializers """
class UpdateCarSerializer(serializers.ModelSerializer):
    car_brand = serializers.CharField(source='car_brand.name')
    car_model = serializers.CharField(source='car_model.name')
    user = serializers.CharField(source='user.username')
    class Meta:
        model = UserCar
        fields=('user','car_brand','car_model','first_reg','odometer')



class CarSerializer(serializers.ModelSerializer):
    car_brand = serializers.CharField(source='car_brand.name')
    car_model = serializers.CharField(source='car_model.name')
    user = serializers.CharField(source='user.username')
    class Meta:
        model = UserCar
        fields=('user','car_brand','car_model','first_reg','odometer')


class CreateCarSerializer(serializers.ModelSerializer):
    car_brand = serializers.CharField(source='car_brand.name')
    car_model = serializers.CharField(source='car_model.name')
    user = serializers.CharField(source='user.username')
    class Meta:
        model = UserCar
        fields = ('user','car_brand','car_model','first_reg','odometer')
