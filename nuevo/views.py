from django.views.generic import TemplateView
<<<<<<< HEAD
from apps.articulo.models import Articulo

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimos_posts'] = Articulo.objects.order_by('-fecha_publicacion')[:5]
        return context
=======


class IndexView(TemplateView):
    template_name = 'index.html'
>>>>>>> 9cab8cd9ecfa8d4a6c09a03c898b285264b754cd
