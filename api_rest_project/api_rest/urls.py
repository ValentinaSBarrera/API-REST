from django import views
from django.urls import path
from .views import  CategoriasView
from .views import  SubcategoriasView
from .views import  TiposView
from .views import  ProductosView
from .views import  UsuariosView
from .views import  UsuarioView
from .views import  ProductosBySupermarketView
from .views import  SupermercadosView
from .views import  MarcasBySupermarketView
from .views import  MarcasView
from .views import ListaCompraView
from .views import obtener_producto_con_logo




urlpatterns = [
    path('categorias', CategoriasView.as_view(), name='categorias_list'),#lista de categorias(GET)
    path('categorias/<int:id_categoria>/subcategorias', SubcategoriasView.as_view(), name='subcategorias_list'),#lista de subcategorias por id de categoria (GET)
    path('subcategorias/<int:id_subcategoria>/tipos', TiposView.as_view(), name='tipos_list'),#lista de tipos por id de subcategoria (GET)
    path('tipos/<int:id_tipo>/productos', ProductosView.as_view(), name='productos_by_Types_list'),#lista de productos por id de tipo (GET)
    path('usuarios', UsuariosView.as_view(), name='usuarios_list'),#lista de usuarios (GET)
    path('usuario', UsuarioView.as_view(), name='usuario_create'),#crear usuario (POST)
    path('usuario/<str:email>/<str:contrasena>', UsuarioView.as_view(), name='usuario'), #login (GET)
    path('usuario/<str:email>', UsuarioView.as_view(), name='usuario_update'), #actualizar usuario por email (PUT)
    path('usuario/<str:email>', UsuarioView.as_view(), name='usuario_delete'), #eliminar usuario por email (DELETE)
    path('producto/<int:id_tipo>', obtener_producto_con_logo, name='productos_list'), #lista de productos (GET)
    path('supermercado/<int:id_supermercado>/productos', ProductosBySupermarketView.as_view(), name='productos_by_Supermarket_list'), #lista de productos por id de supermercado (GET)
    path('supermercados', SupermercadosView.as_view(), name='supermercados_list'),#lista de supermercados (GET)
    path('marcas/<int:id_supermercado>', MarcasBySupermarketView.as_view(), name='marcas_list'), #lista de marcas por id de supermercado (GET)
    path('marcas', MarcasView.as_view(), name='marcas_list'), #lista de marcas (GET)
    path('listacompra/<int:id_usuario>/productos', ListaCompraView.as_view(), name='lista_compra_list'), #lista de productos de la lista de la compra por id de usuario (GET)
    path('listacompra/<int:id_usuario>', ListaCompraView.as_view(), name='lista_compra_create'), #añadir producto a la lista de la compra por id de usuario e id de producto(POST)
    path('listacompra/<int:id_usuario>/producto/<int:id_producto>', ListaCompraView.as_view(), name='lista_compra_delete'), #eliminar producto de la lista de la compra por id de usuario e id de producto (DELETE)

]
