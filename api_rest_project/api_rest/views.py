import json
from django.contrib.auth.hashers import make_password
from typing import Any
from django import http
from django.forms import model_to_dict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Categorias
from .models import Subcategorias
from .models import Tipos
from .models import Productos
from .models import Usuarios
from .models import Supermercados
from .models import Marcas
from .models import ListasDeLaCompra

# Create your views here.

#Lista de Categorias(solo usaremos el metodo get porque no necesitamos agregar, modificar u borrar categorias)
class CategoriasView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):    
            categorias = list(Categorias.objects.values())
            if len(categorias)>0:
                datos = {'Categorias' : categorias}
            else:
                datos = {'message' :" Categories not found.... "}    
            return JsonResponse (datos)


#Lista de Subcategorias por cada categoria(solo usaremos el metodo get porque no necesitamos agregar, modificar u borrar subcategorias)
class SubcategoriasView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id_categoria):
        if id_categoria > 0:
            subcategorias = list(Subcategorias.objects.filter(id_categoria=id_categoria).values())
            if len(subcategorias) > 0:
                datos = {'Subcategorias': subcategorias}
            else:
                datos = {'message': 'Subcategories not found...'}
        else:
            subcategorias = list(Subcategorias.objects.values())
            if len(subcategorias) > 0:
                datos = {'Subcategorias': subcategorias}
            else:
                datos = {'message': 'Subcategories not found...'}
        
        return JsonResponse(datos)


# Lista de tipos de productos por cada subcategoria(solo usaremos el metodo get porque no necesitamos agregar, modificar u borrar tipos)
class TiposView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id_subcategoria):
        if id_subcategoria > 0:
            tipos = list(Tipos.objects.filter(id_subcategoria=id_subcategoria).values())
            if len(tipos) > 0:
                datos = {'Tipos': tipos}
            else:
                datos = {'message': 'Types not found...'}
        else:
            tipos = list(Tipos.objects.values())
            if len(tipos) > 0:
                datos = {'Tipos': tipos}
            else:
                datos = {'message': 'Types not found...'}
        
        return JsonResponse(datos)
    

#Lista de productos por cada tipo de producto(solo usaremos el metodo get porque no necesitamos agregar, actualizar u borrar productos)

class ProductosView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id_tipo):
        if id_tipo > 0:
            productos = list(Productos.objects.filter(tipo=id_tipo).values())
            if len(productos) > 0:
                datos = {'Productos': productos}
            else:
                datos = {'message': 'Products not found...'}
        else:
            productos = list(Productos.objects.values())
            if len(productos) > 0:
                datos = {'Productos': productos}
            else:
                datos = {'message': 'Products not found...'}
        
        return JsonResponse(datos)
    
    

# Lista de usuarios(solo usaremos el metodo get y post porque no necesitamos actualizar u borrar usuarios)    
    
class UsuariosView(View):
    
     @method_decorator(csrf_exempt)
     def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
     def get(self, request, id = 0 ):   
        if id > 0: 
            usuarios = list(Usuarios.objects.filter(id=id).values())
            if len(usuarios)>0:
                usuario = usuarios[0]
                datos = {'Usuario' : usuario}
            else:
                datos = {'message' :" user not found.... "}
            return JsonResponse (datos)    
        else:    
            usuarios = list(Usuarios.objects.values())
            if len(usuarios)>0:
                datos = {'Usuarios' : usuarios}
            else:
                datos = {'message' :" users not found.... "}    
            return JsonResponse (datos)
        
     
        
# Usuario por su nombre de usuario y contraseña(solo usaremos el metodo get, put y delete porque no necesitamos agregar usuarios), 
# solo se puede actualizar y borrar por el email porque es unico
class UsuarioView(View):
     @method_decorator(csrf_exempt)
     def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
     def get(self, request, email, contrasena):   
        if email != None and contrasena != None: 
            usuarios = list(Usuarios.objects.filter(email=email,contrasena=contrasena).values())
            if len(usuarios)>0:
                usuario = usuarios[0]
                datos = {'Usuario' : usuario}
            else:
                datos = {'message' :" usser not found.... "}
            return JsonResponse (datos)    
        else:    
            usuarios = list(Usuarios.objects.values())
            if len(usuarios)>0:
                datos = {'Usuarios' : usuarios}
            else:
                datos = {'message' :" users not found.... "}    
            return JsonResponse (datos)
     def post(self, request):
         
        jd = json.loads(request.body)    
        email = jd.get('email', '')
        email = jd.get('email', '')
        contrasena = jd.get('contrasena', '')
        
        if not email.strip() or not email.strip() or not contrasena.strip():
            datos = {'message': 'Incomplete data...'}
            return JsonResponse(datos)
        elif Usuarios.objects.filter(email=jd['email']).exists():
            datos = {'message': 'User already exists...'}
            return JsonResponse(datos)
        else:
            Usuarios.objects.create(nombre_usuario=jd['nombre_usuario'], email=jd['email'], contrasena=jd['contrasena'])
            datos = {'message': 'success create'}
            return JsonResponse(datos)   
     def put(self, request, email):
        jd = json.loads(request.body)
        usuarios = list(Usuarios.objects.filter(email=email).values())
        if len(usuarios) > 0 :
            usuario = Usuarios.objects.get(email=email)
            usuario.nombre_usuario = jd['nombre_usuario']
            usuario.email = jd['email']
            usuario.contrasena = jd['contrasena']
            usuario.save()
            datos = {'message' : "success update"}
        else:
            datos = {'message' : "user not found.... "}
        return JsonResponse (datos) 
     
     def delete(self, request, email):
        usuarios = list(Usuarios.objects.filter(email=email).values())
        if len(usuarios) > 0 :
            usuario = Usuarios.objects.get(email=email)
            usuario.delete()
            datos = {'message' : "success delete"}   
        else:
            datos = {'message' : "user not found.... "}
        return JsonResponse (datos)
    

#lista de prodcutos de un supermercado(solo usaremos el metodo get porque no necesitamos agregar, actualizar u borrar productos)
class ProductosBySupermarketView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id_supermercado):
        try:
            Supermercados.objects.get(id=id_supermercado)
            marca_ids = Marcas.objects.filter(id_supermercado=id_supermercado).values_list('id', flat=True)
            productos = Productos.objects.filter(marca__in=marca_ids)
            datos = {'Productos': list(productos.values())}
            return JsonResponse(datos)
        except Supermercados.DoesNotExist:
            datos = {'message': 'Supermarket no encontrado'}
            return JsonResponse(datos)


#Lista de supermercados(solo usaremos el metodo get porque no necesitamos agregar, actualizar u borrar supermercados)
class SupermercadosView(View):
    def get(self, request):
        supermercados = list(Supermercados.objects.values())
        if len(supermercados) > 0:
            datos = {'Supermercados': supermercados}
        else:
            datos = {'message': 'Supermarkets not found...'}
        return JsonResponse(datos)

#Lista de marcas de un supermercado(solo usaremos el metodo get porque no necesitamos agregar, actualizar u borrar marcas)
class MarcasBySupermarketView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id_supermercado):
        try:
            Supermercados.objects.get(id=id_supermercado)
            marcas = list(Marcas.objects.filter(id_supermercado=id_supermercado).values())
            if len(marcas) > 0:
                datos = {'Marcas': marcas}
            else:
                datos = {'message': 'Brands not found...'}
            return JsonResponse(datos)
        except Supermercados.DoesNotExist:
            datos = {'message': 'Supermarket no encontrado'}
            return JsonResponse(datos)
        

#lista de marcas (solo usaremos el metodo get porque no necesitamos agregar, actualizar u borrar marcas)
class MarcasView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        marcas = list(Marcas.objects.values())
        if len(marcas) > 0:
            datos = {'Marcas': marcas}
        else:
            datos = {'message': 'Brands not found...'}
        return JsonResponse(datos)


#lista de la compra de un usuario (usaaremos los metodos get, post y delete porque no necesitamos actualizar la lista de la compra) 

class ListaCompraView(View):
    
     @method_decorator(csrf_exempt)
     def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
            return super().dispatch(request, *args, **kwargs)
     def get(self, request, id_usuario):
        try:
            lista_compra = ListasDeLaCompra.objects.filter(id_usuario=id_usuario)

            productos = []
            for item in lista_compra:
                producto = Productos.objects.get(id=item.id_producto_id)
                supermercado = producto.marca.id_supermercado
                logo_supermercado = supermercado.logo_super
                producto_data = {
                    'id': producto.id,
                    'nombre': producto.nombre,
                    'precio': producto.precio,
                    'imagen': producto.imagen,
                    'supermercado': {
                        'logo_super': logo_supermercado
                    }
                    
                }
                productos.append(producto_data)

            respuesta = {
                'ListaCompra': productos
            }

            return JsonResponse(respuesta)

        except ListasDeLaCompra.DoesNotExist:
            datos = {'message': 'Shopping list does not exist...'}
            return JsonResponse(datos, status=404)


     def post(self, request, id_usuario):
            if request.content_type != 'application/json':
                datos = {'message': 'Invalid content type, must be application/json'}
                return JsonResponse(datos, status=400)

            try:
                jd = json.loads(request.body)
                id_producto = jd.get('id_producto', '')

                if not id_producto:
                    datos = {'message': 'Incomplete data...'}
                    return JsonResponse(datos, status=400)

                usuario = get_object_or_404(Usuarios, id=id_usuario)
                producto = get_object_or_404(Productos, id=id_producto)

                if ListasDeLaCompra.objects.filter(id_usuario=usuario, id_producto=producto).exists():
                    datos = {'message': 'Product already exists in the shopping list...'}
                    return JsonResponse(datos, status=400)

                lista_compra = ListasDeLaCompra.objects.create(id_usuario=usuario, id_producto=producto)
                datos = {"producto": model_to_dict(lista_compra)}
                return JsonResponse(datos)

            except json.JSONDecodeError:
                datos = {'message': 'Invalid JSON data'}
                return JsonResponse(datos, status=400)

        
     def delete(self, request, id_usuario, id_producto):
        lista_compra = list(ListasDeLaCompra.objects.filter(id_usuario=id_usuario, id_producto=id_producto).values())
        if len(lista_compra) > 0 :
            lista_compra = ListasDeLaCompra.objects.get(id_usuario=id_usuario, id_producto=id_producto)
            lista_compra.delete()
            datos = {'message' : "success delete"}   
        else:
            datos = {'message' : "product not found in the shopping list.... "}
        return JsonResponse (datos)  

def obtener_producto_con_logo(request, id_tipo):
    productos = Productos.objects.filter(tipo_id=id_tipo)
    lista_productos = []

    for producto in productos:
        supermercado = producto.marca.id_supermercado
        logo_supermercado = supermercado.logo_super
        datos_producto = {
            'nombre': producto.nombre,
            'precio': producto.precio,
            'imagen': producto.imagen,
            'supermercado': {
                'logo_super': logo_supermercado
            }
        }
        lista_productos.append(datos_producto)
    respuesta = {
        'productos': lista_productos
    }
    json_respuesta = json.dumps(respuesta)
    return HttpResponse(json_respuesta, content_type='application/json')

class ApiRestView(View):
    def get(self, request):
        return render(request, 'index.html')