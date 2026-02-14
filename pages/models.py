from django.db import models


class Female (models.Model):
    name_female = models.CharField(max_length=50, null=True)
    
class Male (models.Model):
    name_male = models.CharField(max_length=50, null=True)
    girls = models.OneToOneField(Female, on_delete=models.CASCADE)
    
    
