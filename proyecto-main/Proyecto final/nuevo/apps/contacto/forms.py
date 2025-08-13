from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre_apellido', 'email', 'asunto', 'mensaje']
        labels = {
            'nombre_apellido': 'Nombre y Apellido',
            'email': 'Correo electrónico',
            'asunto': 'Asunto',
            'mensaje': 'Dejanos tu mensaje',
        }