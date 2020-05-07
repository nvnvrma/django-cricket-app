from django.db import models

class points(models.Model):
    teamName = models.CharField(max_length=300,null=False,blank=False)
    points = models.CharField(max_length=300,default='0')
