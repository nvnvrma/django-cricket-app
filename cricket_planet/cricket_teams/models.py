from django.db import models

class cricketTeamsModel(models.Model):
    teamName = models.CharField(max_length=300,null=False,blank=False)
    logoUri = models.CharField(max_length=50,default=None)
    clubState = models.CharField(max_length=100,null=True,blank=True)