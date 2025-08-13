from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
<<<<<<< HEAD
from django.views.generic import View, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Comentario
from .forms import ComentarioForm, EditarComentarioForm
=======
from django.views.generic import View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Comentario
from .forms import ComentarioForm
>>>>>>> 7a84f95b668fa99484bc0501174096f431b6fba4
from apps.articulo.models import Articulo
from apps.usuario.models import Usuario


class ComentarArticuloView(LoginRequiredMixin, View):
    def get(self, request, id):
        articulo = get_object_or_404(Articulo, id=id)
        form = ComentarioForm()
        return render(request, 'comentario/comentar.html', {'form': form, 'articulo': articulo})

    def post(self, request, id):
        articulo = get_object_or_404(Articulo, id=id)
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = articulo
            comentario.usuario = request.user
            comentario.save()
            return redirect('leer_articulo', id=id)
        return render(request, 'comentario/comentar.html', {'form': form, 'articulo': articulo})


class ListadoComentarioView(View):
    def get(self, request):
        comentarios = Comentario.objects.all()
        usuario = request.user.id
        context = {
            'comentarios': comentarios,
            'usuario': usuario,
        }
        return render(request, 'comentario/listadoComentario.html', context)


class AgregarComentarioView(View):
    def get(self, request):
        usuario = Usuario(usuario=request.user)
        form = ComentarioForm()
        context = {
            'form': form,
            'usuario': usuario,
        }
        return render(request, 'comentario/agregarComentario.html', context)

    def post(self, request):
        usuario = Usuario(usuario=request.user)
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            form = ComentarioForm()
        context = {
            'form': form,
            'usuario': usuario,
        }
        return render(request, 'comentario/agregarComentario.html', context)


<<<<<<< HEAD
class EditarComentarioView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comentario
    form_class = EditarComentarioForm
    template_name = 'comentario/editarComentario.html'
    
    def test_func(self):
        """Solo el autor del comentario puede editarlo"""
        comentario = self.get_object()
        return comentario.usuario == self.request.user
    
    def get_success_url(self):
        """Redirige al artículo después de editar el comentario"""
        messages.success(self.request, '¡Comentario editado con éxito!')
        return reverse_lazy('apps.articulo:articulo_detalle', kwargs={'id': self.object.articulo.id})
    
    def form_valid(self, form):
        """Mensaje de éxito al editar"""
        messages.success(self.request, '¡Comentario editado con éxito!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        """Agregar información adicional al contexto"""
        context = super().get_context_data(**kwargs)
        context['comentario'] = self.object
        context['articulo'] = self.object.articulo
        return context


=======
>>>>>>> 7a84f95b668fa99484bc0501174096f431b6fba4
class DeleteComentario(DeleteView):
    model = Comentario
    template_name = 'comentario/eliminarComentario.html'
    
    def get_success_url(self):
        messages.success(self.request, '¡Borrado con éxito!')
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('apps.articulo:articulos')


class DetalleArticuloView(View):
    def get(self, request, articulo_id):
        articulo = Articulo.objects.get(id=articulo_id)
        comentarios = Comentario.objects.filter(articulo=articulo)
        return render(request, 'detalle_articulo.html', {'articulo': articulo, 'comentarios': comentarios})
