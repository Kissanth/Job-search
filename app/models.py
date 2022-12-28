from django.db import models

# Create your models here.
class Postingmodel(models.Model):


    Title = models.CharField(max_length=25)

    Experience = models.IntegerField()

    Email = models.EmailField(default='exampel@hotmail.in')



    
