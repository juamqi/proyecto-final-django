from .models import Articulo,  Categoria
from apps.comentario.models import Comentario
from .forms import ArticuloForm, NuevaCategoriaForm
from apps.comentario.forms import ComentarioForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages

# Todos los artículos
class ArticuloListView(ListView):
    model = Articulo
    template_name = "articulo/articulos.html"
    context_object_name = "articulos"
    paginate_by = 6  # <-- Paginación fija

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # --- Búsqueda ---
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(titulo__icontains=search)
        
        # --- Filtro por categoría ---
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)
        
        # --- Ordenamiento ---
        orden = self.request.GET.get('orden')
        if orden == 'antiguedad_asc':
            queryset = queryset.order_by('fecha_publicacion')
        elif orden == 'antiguedad_desc':
            queryset = queryset.order_by('-fecha_publicacion')
        elif orden == 'alfabetico_asc':
            queryset = queryset.order_by('titulo')
        elif orden == 'alfabetico_desc':
            queryset = queryset.order_by('-titulo')
        else:
            # Orden por defecto
            queryset = queryset.order_by('-fecha_publicacion')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['orden'] = self.request.GET.get('orden', 'antiguedad_desc')
        return context

#Artículo individual
class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = "articulo/post.html" 
    success_url = 'articulos'
    context_object_name = "articulos" 
    pk_url_kwarg = "id" 
    queryset = Articulo.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        context['comentarios'] = Comentario.objects.filter(articulo_id=self.kwargs['id'])
        return context

    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            messages.success(self.request, 'Comentario creado con éxito.')
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.articulo_id = self.kwargs['id']
            comentario.save()
            return redirect('apps.articulo:articulo_detalle', id=self.kwargs['id'])
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

#Artículo creación
class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo/articulo_form.html'

    def form_valid(self, form):
        form.instance.editor = self.request.user
        messages.success(self.request, '¡Artículo creado con éxito!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('apps.articulo:articulos')

#Artículo modificación
class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo/articulo_form.html'

    def form_valid(self, form):
        messages.success(self.request, '¡Artículo modificado con éxito!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('apps.articulo:articulos')

#Articulo borrar
class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'articulo/articulo_eliminar.html'

    def get_success_url(self):
        messages.success(self.request, '¡Borrado con éxito!')
        return reverse_lazy('apps.articulo:articulos')

class ArticuloPorCategoriaView(ListView):
    model = Articulo
    template_name = 'articulo/articulos_por_categoria.html'
    context_object_name = 'articulos'

    def get_queryset(self):
        return Articulo.objects.filter(categoria_id=self.kwargs['pk'])
    
#Categorías
class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = NuevaCategoriaForm
    template_name = 'articulo/crear_categoria.html'

    def get_success_url(self):
        messages.success(self.request, '¡Categoría creada con éxito!')
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('apps.articulo:articulo_crear')

# Lista de Categorías
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'articulo/categoria_lista.html'
    context_object_name = 'categorias'

#Borrar Categorías
class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'articulo/categoria_eliminar.html'
    success_url = reverse_lazy('apps.articulo:categoria_lista')

