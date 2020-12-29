from django.db import models


class FileClass(models.Model):
    file = models.FileField(upload_to='static/')
