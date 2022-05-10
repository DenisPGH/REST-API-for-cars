from django.db import models

# Create your models here.
from django_softdelete.models import SoftDeleteModel

from Cars.users_app.models import TimeHelper, CustomCarUser


class CarBrand(TimeHelper,SoftDeleteModel):
    NAME_CAR_BRAND_LENGHT=100
    name=models.CharField(
        max_length=NAME_CAR_BRAND_LENGHT,
    )

    def __str__(self):
        return f"{self.name}"

# CarModel [car_brand, name, created_at, update_at]

class CarModel(SoftDeleteModel,TimeHelper):
    NAME_CAR_MODEL_MAX_LENGHT = 200
    name=models.CharField(
        max_length=NAME_CAR_MODEL_MAX_LENGHT
    )
    car_brand=models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return f"{self.name}"

#UserCar [user, car_brand, car_model, first_reg, odometer, created_at, deleted_at]

class UserCar(SoftDeleteModel,TimeHelper):
    user=models.ForeignKey(
        CustomCarUser,
        on_delete=models.CASCADE,
    )
    car_brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE,
    )
    car_model = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE,
    )
    first_reg=models.DateField()

    odometer=models.IntegerField(

    )




