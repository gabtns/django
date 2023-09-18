from django.contrib import admin
from .models import modelos
# Register your models here.
class projectAdmin(admin.ModelAdmin):
    # son para ver las fechas de los archivos 
    readonly_fields = ('created','update')  
    #creo los filtros que tendre en el panel de proyectos,se busca los archivos 
    search_fields = ('titulo','created')
    # filtra por archivos
    list_filter = ('titulo',)
    #se ven en columnas las distintas columnas por cada campo elegido.
    list_display = ('id','titulo','descripcion','url','created')

admin.site.register(modelos,projectAdmin)

    
    
