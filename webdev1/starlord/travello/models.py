from django.db import models

# Create your models here.
class Destination(models.Model):
    name= models.CharField(max_length=35)
    description= models.TextField()
    price= models.IntegerField()
    image=  models.ImageField(upload_to='pics')
    offer=  models.BooleanField(default= False)