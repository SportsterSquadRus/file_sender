from django.db import models
import os


class FileClass(models.Model):
    obj = models.FileField(upload_to='static/')

    def __str__(self):
        return os.path.basename(self.obj.name)

