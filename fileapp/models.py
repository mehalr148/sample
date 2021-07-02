from django.db import models
from fileapp.models import *


# Create your models here.
class upload_CV(models.Model):

    myfiles = models.FileField(upload_to='',null=True,blank=True)



