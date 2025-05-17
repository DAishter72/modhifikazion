from django.views.generic import ListView
from django.utils import timezone
from home.models import Promocion, Producto, Categoria

<<<<<<< HEAD
# Create your views here.

def home(request):
    return render(request, 'home.html')
=======

class HomeListView(ListView):
    """Vista para el inicio junto a una lista de promociones"""
    model = Promocion
    template_name = 'home.html'
    context_object_name = 'promociones'

    def get_queryset(self):
        """Filtra solo promociones activas y vigentes"""
        hoy = timezone.now().date()
        return Promocion.objects.filter(
            fecha_inicio__lte=hoy,
            fecha_fin__gte=hoy,
            activa=True
        ).order_by('-fecha_inicio').prefetch_related('productos')

    def get_context_data(self, **kwargs):
        """Agrega contexto adicional a la plantilla"""
        context = super().get_context_data(**kwargs)
        # Puedes agregar más contexto aquí si lo necesitas
        return context


class MenuListView(ListView):
    """Vista para mostrar el menu con productos por categoria"""
    model = Producto
    template_name = 'restaurant/menu.html'
    context_object_name = 'categorias_con_productos'

    def get_queryset(self):
        # Obtener todas las categorías con sus productos disponibles
        return Categoria.objects.filter(
            producto__disponible=True
        ).distinct().prefetch_related(
            'producto_set'  # Optimización para evitar consultas N+1
        ).order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Puedes agregar más contexto aquí si es necesario
        return context


class PromocionListView(ListView):
    """Vista para mostrar promociones activas"""
    model = Promocion
    template_name = 'restaurant/promociones.html'
    context_object_name = 'promociones'
    paginate_by = 10  # Paginación de 10 elementos por página
    ordering = ['-fecha_inicio']  # Ordenar por fecha más reciente primero

    def get_queryset(self):
        """Filtra solo promociones activas y vigentes"""
        hoy = timezone.now().date()
        return Promocion.objects.filter(
            fecha_inicio__lte=hoy,
            fecha_fin__gte=hoy,
            activa=True
        ).order_by('-fecha_inicio').prefetch_related('productos')

    def get_context_data(self, **kwargs):
        """Agrega contexto adicional a la plantilla"""
        context = super().get_context_data(**kwargs)
        # Puedes agregar más contexto aquí si lo necesitas
        return context
>>>>>>> 41abdc3a90d09158f03cc514a312f4e2a83f6864
