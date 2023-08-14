from django.shortcuts import render,redirect
import smtplib
from django.urls import reverse
from email.message import EmailMessage
from . import forms
from .forms import formularios
# Create your views here.

def formulario_(request):
    form = forms.formularios()
    # Se valida el formulario, si el metodo que usa el formulario es el post se valida....

    if request.method== "POST":
        # Si el formato es valido...
        form = forms.formularios(data=request.POST)
        if form.is_valid():
            # Sobre cada uno de las variables que tenemos en el formulario se obtendran los valores que envia el formulario y se guardara. 
       
            nombre = request.POST.get('nombre','')
            empresa = request.POST.get('empresa','')
            email = request.POST.get('mail','')
            texto = request.POST.get('texto','')

            # Creamos el Email
            email = EmailMessage(
            "La app : Nuevo mensaje de un interesado ",
            "De {}  con email  {} \n\nEscribio\n\n {}".format(nombre,email,texto),
            "soygabriel.com",
            ["eduardoalegre02@gmail.com"] )
            try:
                email.send()
                return redirect(reverse('formulario'+"?ok"))
            except:
                return redirect(reverse('formulario'+"?ok2"))
        
    return render(request,"formulario/formulario.html",{"form":form})

def email(nombre,asunto,mail,texto):
    # Se crea el objeto donde se obtendran los metodos
    message = EmailMessage()

    email_subjet = asunto
    direccion_correo = mail
    direccion_envio = "eduardoalegre02@gmail.com"
    message['Subject'] = email_subjet
    message['From'] = direccion_correo
    message['To'] = direccion_envio
    PASSWORD = "JPythonAI2022+J"

    #Cuerpo del mensaje
    message.set_content(texto)

    # SDeclaramos el servidor 
    email_smtp = "smtp.gmail.com"
    server = smtplib.SMTP(email_smtp, '587') 

    # Me identifico en el servidor 
    server.ehlo() 

    # Inicio la conexion segura mediante el puerto TLS.
    server.starttls() 

    # Cargo la cuenta de mi Gmail
    server.login(direccion_envio, PASSWORD) 

    # Envio mi email 
    server.send_message(message) 

    # Cierro la conexion del servidor.
    server.quit()

