from django.db import models
from django.utils.timezone import now

# Create your models here.
class modelos(models.Model):
    titulo = models.CharField(max_length=45,verbose_name="TITULO")
    descripcion = models.TextField(max_length=2000,verbose_name="DESCRIPCION")
    imagen = models.ImageField(verbose_name="IMAGEN",upload_to = 'proyectos')
    url = models.URLField(verbose_name="url")
    url_git = models.URLField(verbose_name="url")
    created = models.DateTimeField(auto_now_add=True,verbose_name="CREADO")
    update = models.DateTimeField(auto_now=True,verbose_name="REVISIÓN")

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"
        #ordering = ['-created'] # Dentro de aqui se le da el order, desde el mas nuevo hasta el mas viejo. 

    def __str__(self) -> str:
        return self.titulo