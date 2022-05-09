from django.contrib import admin

# Register your models here.

# @admin.register(RoboUser)
# class TaskUser(admin.ModelAdmin):
#     list_display = ('password','last_login','email')
from Cars.users_app.models import CustomCarUser


@admin.register(CustomCarUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'username','deleted_at','is_deleted','user_car', 'email', 'first_name',
        'last_name', 'is_staff',

        )