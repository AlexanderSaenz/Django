from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    link = models.URLField(blank=True)  # opcional, por ejemplo a GitHub o demo

    def __str__(self):
        return self.titulo

class MenuItem(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=200)  # podría ser path o enlace externo
    orden = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre