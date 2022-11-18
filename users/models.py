from django.db import models

# Create your models here.
from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from statistics import mode
import string
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    staff=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=200,null=True)
    phone=models.IntegerField(null=True)
    image=models.ImageField(default='avatar.jpg',upload_to='photo')
    def __str__(self):
        return self.staff.username