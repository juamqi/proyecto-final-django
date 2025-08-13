from .models import Usuario
from .forms import RegistroUsuarioForm
from ..articulo.models import Articulo
from ..comentario.models import Comentario
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import Group
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from django import forms


class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión.')
        group = Group.objects.get(name='Registrado')
        self.object.groups.add(group)
        return redirect('apps.usuario:login')

class LoginUsuario(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')
        return reverse('index')
     
class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, 'Logout exitoso')
        return response

class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'usuario/usuario_list.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(is_superuser=True)
        return queryset

class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'usuario/eliminar_usuario.html'
    success_url = reverse_lazy('apps.usuario:usuario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        colaborador_group = Group.objects.get(name='Colaborador')
        es_colaborador = colaborador_group in self.object.groups.all()
        context['es_colaborador'] = es_colaborador
        return context

    def post(self, request, *args, **kwargs):
        eliminar_comentarios = request.POST.get('eliminar_comentarios', False)
        eliminar_posts = request.POST.get('eliminar_posts', False)
        self.object = self.get_object()
        if eliminar_comentarios:
            Comentario.objects.filter(usuario=self.object).delete()

        if eliminar_posts:
<<<<<<< HEAD
            Articulo.objects.filter(editor=self.object).delete()
=======
            Articulo.objects.filter(autor=self.object).delete()
>>>>>>> 7a84f95b668fa99484bc0501174096f431b6fba4
        messages.success(request, f'Usuario {self.object.username} eliminado correctamente')
        return self.delete(request, *args, **kwargs)

class MyPasswordResetView(PasswordResetView):
    template_name = 'registration/recuperar_contraseña.html'

    def get_success_url(self):
        messages.success(self.request, 'Se envió un email de recuperación. Revise su casilla de correo para recuperar su cuenta.')
        return reverse('index')

# Nuevas vistas para el perfil de usuario
class PerfilUsuarioView(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'usuario/perfil.html'
    context_object_name = 'usuario'

    def get_object(self):
        return self.request.user

class EditarPerfilView(LoginRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'usuario/editar_perfil.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'imagen']
    
    def get_object(self):
        return self.request.user
    
    def get_success_url(self):
        messages.success(self.request, 'Perfil actualizado correctamente.')
        return reverse('apps.usuario:perfil')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Perfil actualizado correctamente.')
        return response

class CambiarPasswordView(LoginRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'usuario/cambiar_password.html'
    fields = []
    
    def get_object(self):
        return self.request.user
    
    def get_success_url(self):
        messages.success(self.request, 'Contraseña cambiada correctamente.')
        return reverse('apps.usuario:perfil')
    
    def form_valid(self, form):
        password1 = self.request.POST.get('password1')
        password2 = self.request.POST.get('password2')
        
        if password1 != password2:
            messages.error(self.request, 'Las contraseñas no coinciden.')
            return self.form_invalid(form)
        
        if len(password1) < 8:
            messages.error(self.request, 'La contraseña debe tener al menos 8 caracteres.')
            return self.form_invalid(form)
        
        self.object.set_password(password1)
        self.object.save()
        messages.success(self.request, 'Contraseña cambiada correctamente.')
        return redirect(self.get_success_url())

<<<<<<< HEAD
class MisPublicacionesView(LoginRequiredMixin, ListView):
    model = Articulo
    template_name = 'usuario/mis_publicaciones.html'
    context_object_name = 'articulos'
    paginate_by = 10

    def get_queryset(self):
        return Articulo.objects.filter(editor=self.request.user).order_by('-fecha_publicacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user
        return context


class MisComentariosView(LoginRequiredMixin, ListView):
    model = Comentario
    template_name = 'usuario/mis_comentarios.html'
    context_object_name = 'comentarios'
    paginate_by = 10

    def get_queryset(self):
        return Comentario.objects.filter(usuario=self.request.user).order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user
        return context

=======
>>>>>>> 7a84f95b668fa99484bc0501174096f431b6fba4
