from django.db import models
import os


class FileClass(models.Model):
    obj = models.FileField()
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return os.path.basename(self.obj.name)

