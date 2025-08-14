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
<<<<<<< HEAD

class EditarComentarioForm(forms.ModelForm):
    texto = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': ''}), 
        label='' 
    )

    class Meta:
        model = Comentario
        fields = ['texto']
=======
>>>>>>> 7a84f95b668fa99484bc0501174096f431b6fba4
