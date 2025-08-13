from django.db import models
from django.utils import timezone
from django.conf import settings

class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False, default='Sin categoría')

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    
    titulo = models.CharField(max_length=30, null=False)
    resumen = models.TextField(null=False)
    contenido = models.TextField(null=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='post_default.png')
    publicado = models.DateTimeField(default=timezone.now)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo


class Image(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(null=True, blank=True, upload_to='articulo', default='articulo/post_default.png')

    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        super().delete(using=using, keep_parents=keep_parents)









