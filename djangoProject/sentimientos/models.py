from django.db import models

# Create your models here.
class Comentarios(models.Model):
    comentario = models.CharField(max_length=5000)
    comentario_final = models.CharField(max_length=5000)
    clasificacion = models.SmallIntegerField(null=False)

