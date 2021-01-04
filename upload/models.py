from django.db import models
from django.contrib.postgres.fields import ArrayField
import os


class FileClass(models.Model):
    obj = models.FileField()
    date_pub = models.DateTimeField(auto_now_add=True)
    numbers = ArrayField(models.IntegerField())

    def __str__(self):
        return os.path.basename(self.obj.name)
