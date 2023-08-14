from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.vista_2,name = "web2"),
]

if settings.DEBUG: 
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)