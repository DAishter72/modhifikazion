from django.db import models
from django.core.validators import MinValueValidator


class Categoria(models.Model):
    """Modelo para categorizar los productos (ej: Entradas, Platos principales, Postres, etc.)."""
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"


class Producto(models.Model):
    """Modelo para los productos del menú del restaurante."""
    nombre = models.CharField(
        max_length=100, verbose_name="Nombre del producto")
    descripcion = models.TextField(
        verbose_name="Descripción", blank=True, null=True)
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name="Precio"
    )
    imagen = models.ImageField(
        upload_to="menu/imagenes/",
        verbose_name="Imagen del producto",
        blank=True,
        null=True
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Categoría"
    )
    disponible = models.BooleanField(default=True, verbose_name="¿Disponible?")
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["categoria", "nombre"]
