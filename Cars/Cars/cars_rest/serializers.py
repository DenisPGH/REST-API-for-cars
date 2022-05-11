from rest_framework import serializers

from Cars.cars_rest.models import CarBrand, CarModel, UserCar
from Cars.users_app.models import CustomCarUser

""" users serializers"""
class InfoAllUsersSerializer(serializers.ModelSerializer):
    """show the date from the db"""
    class Meta:
        model = CustomCarUser
        fields = '__all__'


""" car brands serializers """
class CarBrandSerializer(serializers.ModelSerializer):
    #name = OnlyNameCarBrandSerializer(many=True)

    class Meta:
        model = CarBrand
        fields = ('name',)


""" car models serializers """
class CarModelSerializer(serializers.ModelSerializer):
    #name = OnlyNameCarBrandSerializer(many=True)

    class Meta:
        model = CarModel
        fields = '__all__'



""" cars serializers """
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = '__all__'

class CreateCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = ('user','car_brand','car_model','first_reg','odometer')