from django.http import HttpResponse
import datetime
#from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

def saludo (request):
    nombre="Silvia"
    apellido="Benitez"
    fecha_hoy= datetime.datetime.now()

    #doc_externo= open("C:/Users/guejo/Desktop/Practicas Django/Practicas/Practicas/templates/mytemplate.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo= loader.get_template('mytemplate.html')
    #ctx=Context({"nombre_usuario":nombre, "apellido":apellido, "fecha":fecha_hoy, "colores":["naranja","morado","blanco","verde musgo"]})
    #documento=doc_externo.render({"nombre_usuario":nombre, "apellido":apellido, "fecha":fecha_hoy, "colores":["naranja","morado","blanco","verde musgo"]})
    return render(request, "mytemplate.html", {"nombre_usuario":nombre, "apellido":apellido, "fecha":fecha_hoy, "colores":["naranja","morado","blanco","verde musgo"]})

def despedida (request):
    return HttpResponse("Hasta luego, esta vista la hice yo solita! XDD")

def dimefecha (request):
    current_date= datetime.datetime.now()
    return HttpResponse (current_date)

#######vistas con parametros######
def calculoEdad (request,edad, year):
    # edadActual=52
    periodo= year-2023
    edadFutura=edad+periodo
    documento="En el agno %s tendras %s agnos" %(year,edadFutura) 
    return HttpResponse (documento)

def Heredera(request):
    current_date= datetime.datetime.now()
    return render (request, "daugther.html", {"fecha":current_date})

def Heredero(request):
    return render (request, "son2.html")