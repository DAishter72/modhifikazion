from django import forms
from .models import ItemCarrito, Pedido

class ItemCarritoForm(forms.ModelForm):
    class Meta:
        model = ItemCarrito
        fields = ['cantidad', 'observaciones']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'min': 1}),
            'observaciones': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ejemplo: sin cebolla'}),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad < 1:
            raise forms.ValidationError('La cantidad debe ser al menos 1.')
        return cantidad


class PedidoForm(forms.ModelForm):
    METODOS_PAGO = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta de crédito/débito'),
        ('paypal', 'PayPal'),
    ]

    metodo_pago = forms.ChoiceField(choices=METODOS_PAGO, widget=forms.RadioSelect)

    class Meta:
        model = Pedido
        fields = ['nombre', 'direccion', 'metodo_pago']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre completo'}),
            'direccion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Dirección de envío'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.strip():
            raise forms.ValidationError('El nombre es obligatorio.')
        return nombre

    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion')
        if not direccion.strip():
            raise forms.ValidationError('La dirección es obligatoria.')
        return direccion
