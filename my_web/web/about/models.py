from django.db import models


# Create your models here.
class sobre_mi(models.Model):
    titulo = models.CharField(max_length=45,verbose_name="TITULO")
    descripcion = models.TextField(max_length=2000,verbose_name="DESCRIPCION")
    imagen = models.ImageField(verbose_name="IMAGEN",upload_to = 'sobre')

    class Meta:
        verbose_name = "sobre_mi"
        verbose_name_plural = "sobre_mis"
       

    def __str__(self) -> str:
        return self.titulo