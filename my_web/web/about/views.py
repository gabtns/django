from django.shortcuts import render
from .models import sobre_mi

def about_(request):
    demi = sobre_mi.objects.all()
    print(demi)
    return render(request,"about/about.html",{"demi":demi})