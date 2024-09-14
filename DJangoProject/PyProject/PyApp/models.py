from django.db import models # type: ignore

# Create your models here.

class Service(models.Model):
    icon = models.CharField(name='Icon', max_length=50)
    title = models.CharField(name='Title', max_length=100)
    description = models.CharField(name='Description', max_length=500)
    
