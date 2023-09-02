from django.contrib import admin
from gestionPedidos.models import Clientes,Articulos,Pedidos
# Register your models here.

class Clientes_admin(admin.ModelAdmin):
    list_display=("nombre","direccion","email","telefono")
    search_fields=("nombre","email","telefono") #coloca una barra busqueda al inicio

class Articulos_admin(admin.ModelAdmin):
    list_filter=("seccion",) #coloca un filtro en columna lateral derecha

class Pedidos_admin(admin.ModelAdmin):
    list_display=("numero","fecha","entregado")
    list_filter=("fecha",) #coloca un filtro  en columna lateral derecha
    date_hierarchy="fecha" #coloca una barra filtro fechas horizontal en el encabezado

admin.site.register (Clientes,Clientes_admin)
admin.site.register (Articulos,Articulos_admin)
admin.site.register (Pedidos, Pedidos_admin)