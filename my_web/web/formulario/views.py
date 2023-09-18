from django.shortcuts import render,redirect
import smtplib
from django.urls import reverse
from django.core.mail import EmailMessage
from . import forms
from .forms import formularios

from django.contrib import messages
# Create your views here.

def formulario_(request):
    import re

    EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    form = forms.formularios()
    # Se valida el formulario, si el metodo que usa el formulario es el post se valida....

    if request.method== "POST":
        # Si el formato es valido...
        formu = forms.formularios(data=request.POST)
        if formu.is_valid():
            # Sobre cada uno de las variables que tenemos en el formulario se obtendran los valores que envia el formulario y 
            #   se guardara. 
            nombre = request.POST.get('nombre','')
            empresa = request.POST.get('empresa','')
            email = request.POST.get('email','')
            if email and not re.match(EMAIL_REGEX, email):
                raise forms.ValidationError('Invalid email format')
            else:
                email = request.POST.get('email','')
            texto = request.POST.get('texto','')

            # Creamos el Email
            mail = EmailMessage(
            "Gaby : Nuevo mensaje",
            f"Nombre: {nombre}\n  Empresa  {empresa} \n mail {email}\n\nEscribio\n\n {texto}",
            "eduardoalegre02@gmail.com",
            ["eduardoalegre02@gmail.com"],
             reply_to= [email]
               )
            try:
                mail.send()
                return redirect(reverse('formulario') + '?OK')
            except:
                return redirect(reverse('formulario') + '?fail')
        
        
    return render(request,"formulario/formulario.html",{"form":form})

def email(nombre,asunto,mail,texto):
    # Se crea el objeto donde se obtendran los metodos*
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

