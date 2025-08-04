from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    apellido = forms.CharField(max_length=100, label='Apellido')
    dni = forms.CharField(max_length=10, label='DNI')
    email = forms.EmailField(label='Email', required=False)
    fecha_de_nacimiento = forms.DateField(label='Fecha de Nacimiento', input_formats=['%d/%m/%Y'],required=False)
    telefono = forms.CharField(max_length=15, label='Teléfono', required=False)
    direccion = forms.CharField(max_length=200, label='Dirección', required=False)
  

class ProveedorForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    apellido = forms.CharField(max_length=100, label='Apellido')
    dni = forms.CharField(max_length=10, label='DNI')
    email = forms.EmailField(label='Email', required=False)
    telefono = forms.CharField(max_length=15, label='Teléfono', required=False)
    servicio_proveedor = forms.CharField(max_length=100, label='Servicio')
    
         
    
class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Producto')
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción')
    stock = forms.IntegerField(label='Stock')
    fecha_ingreso = forms.DateField(label='Fecha de Ingreso',  input_formats=['%d/%m/%Y'])
    
    