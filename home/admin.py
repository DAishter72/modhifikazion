from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Producto, Promocion


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion_corta')
    search_fields = ('nombre',)
    list_per_page = 20

    def descripcion_corta(self, obj):
        return obj.descripcion[:50] + '...' if obj.descripcion else '-'
    descripcion_corta.short_description = 'Descripción corta'


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_formateado',
                    'categoria', 'disponible', 'imagen_previa')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre', 'descripcion')
    list_editable = ('disponible',)
    list_per_page = 20
    fieldsets = (
        ('Información básica', {
            'fields': ('nombre', 'descripcion', 'categoria')
        }),
        ('Precio y disponibilidad', {
            'fields': ('precio', 'disponible')
        }),
        ('Imagen', {
            'fields': ('imagen',),
            'classes': ('wide',)
        }),
    )

    def precio_formateado(self, obj):
        return f"${obj.precio:,.2f}"
    precio_formateado.short_description = 'Precio'

    def imagen_previa(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.imagen.url)
        return "-"
    imagen_previa.short_description = 'Imagen'


class PromocionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descuento_porcentaje', 'fecha_inicio',
                    'fecha_fin', 'activa', 'productos_count', 'imagen_previa')
    list_filter = ('activa', 'fecha_inicio', 'fecha_fin')
    search_fields = ('nombre', 'descripcion')
    list_editable = ('activa',)
    filter_horizontal = ('productos',)
    list_per_page = 20
    date_hierarchy = 'fecha_inicio'

    def descuento_porcentaje(self, obj):
        return f"{obj.descuento}%"
    descuento_porcentaje.short_description = 'Descuento'

    def productos_count(self, obj):
        return obj.productos.count()
    productos_count.short_description = 'Productos'

    def imagen_previa(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.imagen.url)
        return "-"
    imagen_previa.short_description = 'Imagen'


# Registro de modelos
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Promocion, PromocionAdmin)
