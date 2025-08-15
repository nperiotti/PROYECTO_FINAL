from django import forms
from .models import Producto, Cliente, Proveedor

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'dni', 'email', 'fecha_de_nacimiento', 'telefono', 'direccion']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni', 'email', 'telefono', 'servicio_proveedor']
    
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'stock', 'fecha_ingreso']


    
    