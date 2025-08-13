from django import forms
from .models import Articulo, Categoria

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

class NuevaCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
