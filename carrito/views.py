from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CarritoItem, Plato, Pedido
from django.contrib.auth.models import User
from django.utils import timezone

@login_required
def ver_carrito(request):
    items = CarritoItem.objects.filter(usuario=request.user)
    total = sum(item.plato.precio * item.cantidad for item in items)
    return render(request, 'carrito/carrito.html', {'items': items, 'total': total})

@login_required
def agregar_al_carrito(request, plato_id):
    plato = get_object_or_404(Plato, id=plato_id)
    item, created = CarritoItem.objects.get_or_create(usuario=request.user, plato=plato)
    
    if not created:
        item.cantidad += 1
    item.save()
    return redirect('ver_carrito')

@login_required
def editar_item_carrito(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id, usuario=request.user)
    if request.method == 'POST':
        item.cantidad = int(request.POST.get('cantidad', 1))
        item.observaciones = request.POST.get('observaciones', '')
        item.save()
        return redirect('ver_carrito')
    return render(request, 'carrito/editar_item.html', {'item': item})

@login_required
def eliminar_item_carrito(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id, usuario=request.user)
    item.delete()
    return redirect('ver_carrito')

@login_required
def confirmar_pedido(request):
    items = CarritoItem.objects.filter(usuario=request.user)
    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        metodo_pago = request.POST.get('metodo_pago')

        pedido = Pedido.objects.create(
            usuario=request.user,
            direccion=direccion,
            metodo_pago=metodo_pago,
            fecha=timezone.now()
        )
        # Aquí podrías guardar los ítems del carrito dentro del pedido si tu modelo lo permite

        items.delete()  # Vaciar el carrito
        return render(request, 'carrito/pedido_confirmado.html', {'pedido': pedido})

    total = sum(item.plato.precio * item.cantidad for item in items)
    return render(request, 'carrito/confirmar_pedido.html', {'items': items, 'total': total})
