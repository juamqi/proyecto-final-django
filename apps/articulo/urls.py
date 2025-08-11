from django.urls import path
from .views import *

app_name = 'apps.articulo'

urlpatterns = [
    path('articulos/', ArticuloListView.as_view(), name='articulos'),#Ver todos los artículos
    path('articulos/<int:id>', ArticuloDetailView.as_view(), name="articulo_detalle"),#Ver un artículo individual
    path('articulo/crear/', ArticuloCreateView.as_view(), name='articulo_crear'),#Crear un artículo
    path('articulos/<int:pk>/actualizar/', ArticuloUpdateView.as_view(), name='articulo_actualizar'),#Modificar un artículo
    path('articulos/<int:pk>/eliminar/', ArticuloDeleteView.as_view(), name='articulo_eliminar'),#Eliminar un artículo
    path('categoria/', CategoriaListView.as_view(), name='categoria_lista'),
    path('categoria/<int:pk>/articulos/', ArticuloPorCategoriaView.as_view(), name='articulos_por_categoria'),
    path('articulo/categoria', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categoria/<int:pk>/delete/', CategoriaDeleteView.as_view(), name='categoria_delete'),
]
