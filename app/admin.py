from django.contrib import admin
from .models import Categoria, Usuario, Link, Auxiliar, Inventario, Mensajes, Substrata, SubstrataGeneral, SubstrataCataloged

admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Link)
admin.site.register(Auxiliar)
admin.site.register(Inventario)
admin.site.register(Mensajes)
admin.site.register(Substrata)
admin.site.register(SubstrataGeneral)
admin.site.register(SubstrataCataloged)
