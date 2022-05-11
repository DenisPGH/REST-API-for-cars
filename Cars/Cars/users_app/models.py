from django.db import models
from django.contrib.auth.models import AbstractUser
from django_softdelete.models import SoftDeleteModel


class TimeHelper(models.Model):
    """this class store the date info for creating"""
    created_at= models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )
    class Meta:
        abstract=True



class CustomCarUser(AbstractUser,SoftDeleteModel,TimeHelper):
    user_car= models.CharField(
        max_length=20,
        null=True,

    )

