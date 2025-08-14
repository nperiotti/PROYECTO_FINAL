from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path('crear-cliente/', views.crear_cliente, name='crear-cliente'),
path("listar-clientes/", views.listar_clientes, name="listar-clientes"),
path("crear-proveedor/", views.crear_proveedor, name="crear-proveedor"),
path("listar-proveedores/", views.listar_proveedores, name="listar-proveedores"),
path('clientes/buscar/', views.buscar_cliente, name='buscar-cliente'),
path('proveedores/buscar/',  views.buscar_proveedor, name='buscar-proveedores'),


# Vistas basadas en clases para productos
path("crear-producto/", views.ProductoCreateView.as_view(), name="crear-producto"),
path("listar-productos/", views.ProductoListView.as_view(), name="listar-productos"),
path('detalle-producto/<int:pk>/', views.ProductoDetailView.as_view(), name='detalle-producto'),
path('editar-producto/<int:pk>/', views.ProductoUpdateView.as_view(), name='editar-producto'),
path('eliminar-producto/<int:pk>/', views.ProductoDeleteView.as_view(), name='eliminar-producto'),
path('productos/buscar/', views.buscar_productos, name='buscar-productos'),
path('about/', views.about, name='about'),
path('detalle-cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='detalle-cliente'),
path('eliminar-cliente/<int:pk>/', views.ClienteDeleteView.as_view(), name='eliminar-cliente'),
path('detalle-proveedor/<int:pk>/', views.ProveedorDetailView.as_view(), name='detalle-proveedor'),
path('eliminar-proveedor/<int:pk>/', views.ProveedorDeleteView.as_view(), name='eliminar-proveedor'),
]

