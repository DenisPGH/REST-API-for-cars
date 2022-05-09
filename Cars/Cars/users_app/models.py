from django.db import models
from django.contrib.auth.models import AbstractUser
from django_softdelete.models import SoftDeleteModel


class CustomCarUser(AbstractUser,SoftDeleteModel):
    user_car= models.CharField(
        max_length=20,
        null=True,

    )

