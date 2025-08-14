from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Proveedor, Producto
from .forms import ClienteForm, ProveedorForm, ProductoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView   
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# VISTAS BASADAS EN FUNCIONES

# Crear vista para la página de inicio

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'App_Usuarios/about.html')

# Crear cliente, proveedor y producto

@login_required
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
            form = ClienteForm()  # Reciclo el formulario para que esté vacío después de guardar
            return render(request, 'App_Usuarios/crear-cliente.html', {"form": form})
            

    form = ClienteForm()
    return render(request, 'App_Usuarios/crear-cliente.html', {"form": form})

@login_required
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
            form = ProveedorForm()  # Reciclo el formulario para que esté vacío después de guardar
            return render(request, 'App_Usuarios/crear-proveedor.html', {"form": form})

    form = ProveedorForm()
    return render(request, 'App_Usuarios/crear-proveedor.html', {"form": form})

        
# Listar clientes, proveedores y productos

@login_required
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'App_Usuarios/listar-clientes.html', {"clientes": clientes})

@login_required
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'App_Usuarios/listar-proveedores.html', {"proveedores": proveedores})


# Buscar clientes, proveedores y productos
@login_required
def buscar_cliente(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', 'nombre')
        apellido = request.GET.get('apellido', 'apellido')
        clientes = Cliente.objects.filter(nombre__icontains=nombre)
        return render(request, 'App_Usuarios/buscar-cliente.html', {"clientes": clientes, "apellido": apellido, "nombre": nombre})

@login_required
def buscar_proveedor(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        apellido = request.GET.get('apellido', '')
        servicio_proveedor = request.GET.get('servicio_proveedor', '')
                
        proveedores = Proveedor.objects.all()
        
        if nombre:
            proveedores = proveedores.filter(nombre__icontains=nombre)
        if apellido:
            proveedores = proveedores.filter(apellido__icontains=apellido)
        if servicio_proveedor:
            proveedores = proveedores.filter(servicio_proveedor__icontains=servicio_proveedor)

        return render(request, 'App_Usuarios/buscar-proveedores.html', {
            "proveedores": proveedores, 
            "apellido": apellido, 
            "nombre": nombre, 
            "servicio_proveedor": servicio_proveedor
            })

@login_required
def buscar_productos(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        productos = Producto.objects.filter(nombre__icontains=nombre)
        return render(request, 'App_Usuarios/buscar-productos.html', {"productos": productos})

@login_required
def buscar_cliente(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', 'nombre')
        apellido = request.GET.get('apellido', 'apellido')
        clientes = Cliente.objects.filter(nombre__icontains=nombre)
        return render(request, 'App_Usuarios/buscar-cliente.html', {"clientes": clientes, "apellido": apellido, "nombre": nombre})



#VISTAS BASADAS EN CLASES

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'App_Usuarios/crear-producto.html'
    success_url = reverse_lazy('listar-productos')

class ProductoListView(ListView):
    model = Producto
    template_name = 'App_Usuarios/listar-productos.html'
    context_object_name = 'productos'

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'App_Usuarios/crear-producto.html'
    success_url = reverse_lazy('listar-productos')

class ProductoDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = 'App_Usuarios/detalle-producto.html'
    context_object_name = 'producto'

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'App_Usuarios/eliminar-producto.html'
    success_url = reverse_lazy('listar-productos')

class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'App_Usuarios/detalle-cliente.html'
    context_object_name = 'cliente'

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'App_Usuarios/eliminar-cliente.html'
    success_url = reverse_lazy('listar-clientes')

class ProveedorDetailView(LoginRequiredMixin, DetailView):
    model = Proveedor
    template_name = 'App_Usuarios/detalle-proveedor.html'
    context_object_name = 'proveedor'

class ProveedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Proveedor
    template_name = 'App_Usuarios/eliminar-proveedor.html'
    success_url = reverse_lazy('listar-proveedores')


# Create your views here.
