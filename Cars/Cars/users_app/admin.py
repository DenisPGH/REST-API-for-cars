from django.contrib import admin
from Cars.users_app.models import CustomCarUser


@admin.register(CustomCarUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'username','deleted_at','is_deleted', 'email', 'first_name',
        'last_name', 'is_staff',

        )