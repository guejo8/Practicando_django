from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
# Create your views here.
def busqueda_productos(request):
    return render (request,"formulario.html")

def buscar (request):
    if request.GET["product"]:
       # msj= "Articulo buscado:%s" %request.GET ["product"]
       prod= request.GET["product"]
       articulos=Articulos.objects.filter(nombre__icontains=prod)
       return render (request, "resultados_busqueda.html",{"articulos":articulos,"query":prod})

    else:
        msj="No se ha introducido ningun elemento de consulta"
    return HttpResponse (msj)