from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Comentario
from .forms import ComentarioForm
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
