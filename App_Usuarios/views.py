from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Proveedor, Producto
from .forms import ClienteForm, ProveedorForm, ProductoForm


# Crear vista para la página de inicio

def home(request):
    return render(request, 'home.html')

# Crear cliente, proveedor y producto

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = Cliente(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                dni=form.cleaned_data['dni'],
                email=form.cleaned_data['email'],
                fecha_de_nacimiento=form.cleaned_data['fecha_de_nacimiento'],
                telefono=form.cleaned_data['telefono'],
                direccion=form.cleaned_data['direccion']
            )
            cliente.save()
            form = ClienteForm()  # Reset, devuelve el formulario vacío después de guardar
            return render(request, 'App_Usuarios/crear-cliente.html', {"form": form})

    form = ClienteForm()
    return render(request, 'App_Usuarios/crear-cliente.html', {"form": form})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            proveedor = Proveedor(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                dni=form.cleaned_data['dni'],
                email=form.cleaned_data['email'],
                telefono=form.cleaned_data['telefono'],
                servicio_proveedor=form.cleaned_data['servicio_proveedor']
            )
            proveedor.save()
            form = ProveedorForm()  # Reset, devuelve el formulario vacío después de guardar
            return render(request, 'App_Usuarios/crear-proveedor.html', {"form": form})

    form = ProveedorForm()
    return render(request, 'App_Usuarios/crear-proveedor.html', {"form": form})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = Producto(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                stock=form.cleaned_data['stock'],
                fecha_ingreso=form.cleaned_data['fecha_ingreso']
            )
            producto.save()
            form = ProductoForm() # Reset, devuelve el formulario vacío después de guardar
            return render(request, 'App_Usuarios/crear-producto.html', {"form": form})

    form = ProductoForm()
    return render(request, 'App_Usuarios/crear-producto.html', {"form": form})
 
        
# Listar clientes, proveedores y productos

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'App_Usuarios/listar-clientes.html', {"clientes": clientes})


def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'App_Usuarios/listar-proveedores.html', {"proveedores": proveedores})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'App_Usuarios/listar-productos.html', {"productos": productos})


def buscar_proveedor(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', 'apellido')
        apellido = request.GET.get('apellido', 'nombre')
        servicio_proveedor = request.GET.get('servicio_proveedor', 'servicio_proveedor')
        proveedores = Proveedor.objects.filter(nombre__icontains=nombre)
        return render(request, 'App_Usuarios/listar-proveedores.html', {"apellido": apellido, "nombre": nombre, "servicio_proveedor": servicio_proveedor})


# Create your views here.
