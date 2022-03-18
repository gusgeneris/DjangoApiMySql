from django.db import models

# Create your models here.

class Instituciones(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.URLField()
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    
    def __str__(self):
        return self.nombre