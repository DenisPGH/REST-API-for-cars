from django.contrib import admin

# Register your models here.
from Cars.cars_rest.models import CarBrand,CarModel,UserCar


@admin.register(CarBrand)
class TaskCarBrand(admin.ModelAdmin):
    list_display = (
        'name','deleted_at','is_deleted','created_at','updated_at'
        )

@admin.register(CarModel)
class TaskCarModel(admin.ModelAdmin):
    list_display = (
        'name','car_brand','deleted_at','is_deleted','created_at','updated_at'
        )


@admin.register(UserCar)
class TaskUserCar(admin.ModelAdmin):
    list_display = (
        'user','car_brand','car_model','first_reg','odometer',
        'deleted_at','is_deleted','created_at','updated_at'
        )
