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
    HOMETOWN_MAX_LENGHT=20

    data_birth=models.DateField(
        null=True,
    )
    hometown=models.CharField(
        max_length=HOMETOWN_MAX_LENGHT,
        null=True
    )
    picture=models.ImageField(
        upload_to='media',
        null=True,
    )
