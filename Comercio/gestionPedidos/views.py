from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import formulario_contacto
from django.core.mail import EmailMessage


# Create your views here.
def busqueda_productos(request):
    return render (request,"formulario.html")

def buscar (request):
    if request.GET["product"]:
       # msj= "Articulo buscado:%s" %request.GET ["product"]
       prod= request.GET["product"]
       if len(prod)>50:
           msj="texto introducido demasiado largo, prueba de nuevo"
       else:
           
           articulos=Articulos.objects.filter(nombre__icontains=prod)
           return render (request, "resultados_busqueda.html",{"articulos":articulos,"query":prod})
    else:
        msj="No se ha introducido ningun elemento de consulta"
    return HttpResponse (msj)

#METODO DE CREACION MANUAL DE FORMULARIOS (ha funcionado)

# def contacto (request):
#     if request.method=="POST":
#         subject=request.POST["asunto"]
#         message=request.POST["mensaje"] + request.POST["email"]
#         email_from= settings.EMAIL_HOST_USER
#         recipient_list=["midireccion@gmail.com"]
#         send_mail(subject,message,email_from,recipient_list)

#         return render (request,"gracias.html")
    
#     return render(request,"contacto.html")

#METODO DE CREACION FORMULARIO CON API FORMS

def contacto (request):
    if request.method=="POST":
        miform=formulario_contacto(request.POST)
        if miform.is_valid():
            info=miform.cleaned_data
            send_mail(info['asunto'],info['mensaje'],info.get('email',''),['guejo432@gmail.com'],)

            return render (request,"gracias.html")

    else:
        miform=formulario_contacto()
    return render (request,"contacto2.html",{"form":miform})