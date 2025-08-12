from django.urls import path
from . import views

urlpatterns = [
    path('nosotros/', views.Nosotros.as_view(), name='nosotros'),
]