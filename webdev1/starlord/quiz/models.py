from django.db import models
from django.forms.fields import MultipleChoiceField
from django.forms.widgets import RadioSelect


# Create your models here.
class Question(models.Model):
    question= models.TextField()
    op1= models.BooleanField(default=False)
    option1= models.CharField(max_length=50)
    op2= models.BooleanField(default=False)
    option2= models.CharField(max_length=50)
    op3= models.BooleanField(default=False)
    option3= models.CharField(max_length=50)
    op4= models.BooleanField(default=False)
    option4= models.CharField(max_length=50)
    next=models.IntegerField(default=0)
    