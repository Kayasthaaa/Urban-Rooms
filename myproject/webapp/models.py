from distutils.command.upload import upload
from email.mime import image
from unicodedata import name
from django.db import models
import os
from django.contrib.auth.models import User
import datetime

def filepath(request,filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s", (timeNow, old_filename)
    return os.path.join('uploads/', filename)
    

class Room(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500)
    email=models.EmailField(null=True)
    phone_number=models.BigIntegerField()
    location=models.CharField(max_length=100)
    price=models.IntegerField()
    internet=models.BooleanField(default=False)
    parking= models.BooleanField(default=False)
    #photo1 = models.ImageField(upload_to="room", blank=True)
    #photo2 = models.ImageField(upload_to="room", blank=True)
    


    class Meta:
        # This helps to order the data in the admin portion
        ordering = ['-created']

    def str(self) -> str:
        return f'{self.title}'
