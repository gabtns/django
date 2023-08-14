from django.contrib import admin
from .models import modelos
# Register your models here.
class projectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')

#Se debe registrar la clase dentro de el admin.     
admin.site.register(modelos,projectAdmin)
