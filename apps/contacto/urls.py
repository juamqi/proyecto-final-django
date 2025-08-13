from django.urls import path
from . import views

urlpatterns = [
    path('contacto/', views.ContactoUsuario.as_view(), name='contacto'),
]