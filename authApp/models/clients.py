from django.db import models

class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    numerodocumento = models.CharField('Número de documento', max_length = 30)
    nombrecompleto = models.CharField('Nombre completo', max_length = 30)
    direccion = models.CharField('Dirección', max_length = 30)
    municipio = models.CharField('Municipio', max_length = 30)
    departamento = models.CharField('Departamento', max_length = 30)
    correocontacto = models.EmailField('Email', max_length = 100)
    telefonocontacto = models.CharField('Teléfono ', max_length = 30)