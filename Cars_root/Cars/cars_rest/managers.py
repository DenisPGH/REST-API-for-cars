
from django.db import models



class NotDeletedManager(models.Manager):
    """ custom manager, for showing only the not deleted objects"""
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)