from django.db import models

class cricketPlayer(models.Model):
    firstName = models.CharField(max_length=300,null=False,blank=False)
    lastName = models.CharField(max_length=300,null=False,blank=False)
    imageUri = models.CharField(max_length=300,null=True,blank=True, default=None)
    playerJerseyNo = models.IntegerField(null=False,blank=False)
    country = models.CharField(max_length=10,null=True,blank=True)
    matches = models.IntegerField(default='0')
    runs = models.IntegerField(default='0')
    highestScore = models.IntegerField(default='0')
    fifties = models.IntegerField(default='0')
    hundreds = models.IntegerField(default='0')
