from django.contrib import admin
from .models import Plato, Carrito, CarritoItem

admin.site.register(Plato)
admin.site.register(Carrito)
admin.site.register(CarritoItem)
