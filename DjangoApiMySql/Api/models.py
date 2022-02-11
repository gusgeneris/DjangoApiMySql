from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.URLField()
    createdDate = models.DateField()
    
    
