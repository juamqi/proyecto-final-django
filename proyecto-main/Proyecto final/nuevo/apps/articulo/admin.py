from django.contrib import admin
from .models import Categoria, Articulo

# Register your models here.

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'resumen', 'contenido', 'fecha_publicacion',
                    'activo', 'categoria', 'imagen', 'publicado', 'editor')

admin.site.register(Categoria)