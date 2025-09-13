from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    link = models.URLField(blank=True)  # opcional, por ejemplo a GitHub o demo

    def __str__(self):
        return self.titulo
