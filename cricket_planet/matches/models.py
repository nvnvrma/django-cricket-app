from django.db import models

class matches(models.Model):
    matchTeamOne = models.CharField(max_length=300,null=False,blank=False)
    matchTeamTwo = models.CharField(max_length=300,null=False,blank=False)
    winner       = models.CharField(max_length=300,null=False,blank=False)

