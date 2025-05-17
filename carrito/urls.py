from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:plato_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('editar/<int:item_id>/', views.editar_item_carrito, name='editar_item_carrito'),
    path('eliminar/<int:item_id>/', views.eliminar_item_carrito, name='eliminar_item_carrito'),
    path('confirmar/', views.confirmar_pedido, name='confirmar_pedido'),
]
