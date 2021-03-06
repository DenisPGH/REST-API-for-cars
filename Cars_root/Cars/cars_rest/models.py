from datetime import datetime
from django.db import models
from django_softdelete.models import SoftDeleteModel
from Cars_root.Cars.cars_rest.managers import NotDeletedManager
from Cars_root.Cars.users_app.models import TimeHelper, CustomCarUser, TimeCreated



class DeletedAt(models.Model):
    """ my soft delete class """
    objects = NotDeletedManager()
    all_objects_in_db=models.Manager() # for testing
    deleted_at = models.DateTimeField(
        null=True,
    )

    def delete(self, *args, **kwargs):
        self.deleted_at = datetime.now()
        self.save()

    class Meta:
        abstract=True





class CarBrand(TimeCreated, DeletedAt):
    NAME_CAR_BRAND_LENGHT=10
    name=models.CharField(
        max_length=NAME_CAR_BRAND_LENGHT,
    )

    def __str__(self):
        return f"{self.name}"

# CarModel [car_brand, name, created_at, update_at]

class CarModel(TimeHelper, DeletedAt):
    NAME_CAR_MODEL_MAX_LENGHT = 30
    name=models.CharField(
        max_length=NAME_CAR_MODEL_MAX_LENGHT
    )
    car_brand=models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE,
        #related_name='id',
    )
    def __str__(self):
        return f"{self.name}"

#UserCar [user, car_brand, car_model, first_reg, odometer, created_at, deleted_at]

class UserCar(TimeCreated, DeletedAt):
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




