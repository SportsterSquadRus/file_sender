from django.db import models
import os

class Number(models.Model):
    num = models.IntegerField()

    def __str__(self):
        return str(self.num)


class FileClass(models.Model):
    obj = models.FileField()
    date_pub = models.DateTimeField(auto_now_add=True)
    numbers = models.ManyToManyField(Number)
    

    def __str__(self):
        return os.path.basename(self.obj.name)



    
