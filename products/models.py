from django.db import models
from datetime import datetime
# Create your models here.

class Product (models.Model):
    
    x = [
        ('phone','phone'),
        ('computer', 'computer'),
    ]
    
    name = models.CharField(max_length=50, default='name',verbose_name='title')
    content = models.TextField(null=True,blank=True, verbose_name='description')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10.0)
    image = models.ImageField(upload_to='photos/%y/%m/%d',verbose_name='photo')
    category = models.CharField(max_length=50,null =True,blank=True,choices=x)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    class Meta:   # meta class for some apply some feature like ordering , naming and other feature
        ordering = ['-price'] # minus for desc and without - is asc


class Test (models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    created = models.DateTimeField(default=datetime.now)