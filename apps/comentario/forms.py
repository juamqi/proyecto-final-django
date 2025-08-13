from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    texto = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': ''}), 
        label='' 
    )

    class Meta:
        model = Comentario
        fields = ['texto']


class EditarComentarioForm(forms.ModelForm):
    texto = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Escribe tu comentario aquí...',
            'rows': 4,
            'class': 'form-control'
        }), 
        label='Editar Comentario',
        required=True
    )

    class Meta:
        model = Comentario
        fields = ['texto']
