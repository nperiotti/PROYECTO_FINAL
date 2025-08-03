from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    apellido = forms.CharField(max_length=100, label='Apellido')
    dni = forms.IntegerField(label='DNI')
    email = forms.EmailField(label='Email')
    fecha_de_nacimiento = forms.DateField(label='Fecha de Nacimiento')
    telefono = forms.IntegerField(label='Teléfono', required=False)
    direccion = forms.CharField(max_length=200, label='Dirección', required=False)
  

class ProveedorForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    apellido = forms.CharField(max_length=100, label='Apellido')
    dni = forms.IntegerField(label='DNI')
    email = forms.EmailField(label='Email')
    telefono = forms.IntegerField(label='Teléfono')
    servicio_proveedor = forms.CharField(max_length=100, label='Servicio')
    
         
    
class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Producto')
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción')
    stock = forms.IntegerField(label='Stock')
    fecha_ingreso = forms.DateField(label='Fecha de Ingreso')
    
    