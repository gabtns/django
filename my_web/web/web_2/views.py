from django.shortcuts import render
from .models import modelos
# Create your views here.
def vista_2(request):
    modelo = modelos.objects.all()
    
    return render(request,"web_2/proyectos.html", {"modelo":modelo})