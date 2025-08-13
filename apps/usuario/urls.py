from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegistrarUsuario, LoginUsuario, LogoutUsuario, UsuarioListView, UsuarioDeleteView, MyPasswordResetView, PerfilUsuarioView, EditarPerfilView, CambiarPasswordView, MisPublicacionesView, MisComentariosView

app_name = 'apps.usuario'

urlpatterns = [
    path('registrar/', RegistrarUsuario.as_view(), name='registrar'),
    path('login/', LoginUsuario.as_view(), name='login'),
    path('logout/', LogoutUsuario.as_view(), name='logout'),
    path('password_reset/', MyPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),
    path('usuario/<int:pk>/eliminar/', UsuarioDeleteView.as_view(), name='usuario_delete'),
    # Nuevas URLs para el perfil
    path('perfil/', PerfilUsuarioView.as_view(), name='perfil'),
    path('perfil/editar/', EditarPerfilView.as_view(), name='editar_perfil'),
    path('perfil/cambiar-password/', CambiarPasswordView.as_view(), name='cambiar_password'),
    path('perfil/mis-publicaciones/', MisPublicacionesView.as_view(), name='mis_publicaciones'),
    path('perfil/mis-comentarios/', MisComentariosView.as_view(), name='mis_comentarios'),
]
