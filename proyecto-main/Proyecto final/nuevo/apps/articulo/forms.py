from django import forms
from .models import Articulo, Categoria

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
<<<<<<< HEAD
        fields = ['titulo', 'contenido', 'categoria', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }
=======
        fields = '__all__'
>>>>>>> 7a84f95b668fa99484bc0501174096f431b6fba4

class NuevaCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
<<<<<<< HEAD
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
=======
        fields = '__all__'
>>>>>>> 7a84f95b668fa99484bc0501174096f431b6fba4
