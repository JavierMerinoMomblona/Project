from django.contrib import admin
from .models import Categoria, Usuario, Link, Archivo, Auxiliar, Inventario, Mensajes, SustratosOriginales, SustratosCatalogados

admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Link)
admin.site.register(Archivo)
admin.site.register(Auxiliar)
admin.site.register(Inventario)
admin.site.register(Mensajes)
admin.site.register(SustratosOriginales)
admin.site.register(SustratosCatalogados)
