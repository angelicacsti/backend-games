from django.db import models

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    codigoproducto = models.CharField('Código', max_length = 30)
    categoriaproducto = models.CharField('Categoría de producto', max_length = 30)
    descripcion = models.CharField('Descripción', max_length = 30)
    genero = models.CharField('Género', max_length = 30)
    precio = models.IntegerField(default=0)
    unidadesdisponibles = models.IntegerField(default=0)

