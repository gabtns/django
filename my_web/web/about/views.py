from django.shortcuts import render
from .models import sobre_mi

def about_(request):
    demi = sobre_mi.objects.all()
   
    return render(request,"about/about.html",{"demi":demi})