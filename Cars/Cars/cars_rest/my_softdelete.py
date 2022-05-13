from datetime import datetime

from django.db import models


# class MySoftDelete(models.Model):
#     deleted_at=models.DateTimeField(
#         default=None
#     )
#     def delete(self, *args, **kwargs):
#         self.deleted_at = datetime.now()
#         self.save()