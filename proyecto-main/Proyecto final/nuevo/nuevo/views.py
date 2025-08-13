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
>>>>>>> 7a84f95b668fa99484bc0501174096f431b6fba4
