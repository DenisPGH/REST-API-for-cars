from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomCarUser(AbstractUser):
    user_car= models.CharField(
        max_length=20,
        null=True,

    )

