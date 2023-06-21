from django.contrib import admin
from .models import Categorias
from .models import ListasDeLaCompra
from .models import Marcas
from .models import Productos
from .models import Subcategorias
from .models import Supermercados
from .models import Tipos
from .models import Usuarios

# Register your models here.

admin.site.register(Categorias)
admin.site.register(ListasDeLaCompra)
admin.site.register(Marcas)
admin.site.register(Productos)
admin.site.register(Subcategorias)
admin.site.register(Supermercados)
admin.site.register(Tipos)
admin.site.register(Usuarios)
