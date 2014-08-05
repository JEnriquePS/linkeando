from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    titulo = models.CharField(max_length=140)

    def __unicode__(self):
        return self.titulo


class Enlace(models.Model):
    def image_path(self, filename):
        ruta = "{0}/{1}/{2}".format(self.categoria, self.titulo, str(filename))
        return ruta

    titulo = models.CharField(max_length=140)
    enlace = models.URLField()
    votos = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria)
    usuario = models.ForeignKey(User)
    img_enlace = models.ImageField(upload_to=image_path)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{0}-{1}".format(self.titulo, self.enlace)

    def mis_votos_en_imagen_rosada(self):
        return 'http://placehold.it/200x100/E8117F/ffffff/&text=%d+votos' % self.votos

    def es_popular(self):
        return self.votos > 10
    es_popular.boolean = True


class Agregador(models.Model):
    titulos = models.CharField(max_length=140)
    enlace = models.ManyToManyField(Enlace)
