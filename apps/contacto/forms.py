from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
<<<<<<< HEAD
        fields = ['nombre_apellido', 'email', 'asunto', 'mensaje']
        labels = {
            'nombre_apellido': 'Nombre y Apellido',
            'email': 'Correo electrónico',
            'asunto': 'Asunto',
            'mensaje': 'Dejanos tu mensaje',
        }
=======
        fields = ['nombre_apellido', 'email', 'asunto', 'mensaje']
>>>>>>> 7a84f95b668fa99484bc0501174096f431b6fba4
