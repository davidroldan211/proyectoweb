from django.db import models

# Create your models here.
class Servicio(models.Model):
    titulo=models.CharField(max_length=20)
    contenido=models.CharField(max_length=20)
    imagen=models.ImageField()
    created=models.DateField(auto_now_add=True) #en estos modelos se suele usar muy frecuentemente estos campos para ordenar el contenido por fecha y por actualizacion
    updated=models.DateField(auto_now_add=True)
    class Meta: # Esta clase se usa para especificar diferentes parametros que pueda tener nuetro modelo
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    def __str__(self):
        return self.titulo