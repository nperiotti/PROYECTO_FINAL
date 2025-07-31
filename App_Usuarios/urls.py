from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path('crear-cliente/', views.crear_cliente, name='crear-cliente'),
path("listar-clientes/", views.listar_clientes, name="listar-clientes"),
path("crear-proveedor/", views.crear_proveedor, name="crear-proveedor"),
path("listar-proveedores/", views.listar_proveedores, name="listar-proveedores"),
path('proveedores/buscar',  views.buscar_proveedor, name='buscar-proveedor'),
path("crear-producto/", views.crear_producto, name="crear-producto"),
path("listar-productos/", views.listar_productos, name="listar-productos"),

]