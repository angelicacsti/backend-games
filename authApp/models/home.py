from django.db import models

class Home(models.Model):
    id = models.AutoField(primary_key=True)
    nit = models.CharField('NIT', max_length = 30)
    nombrecomercial = models.CharField('Nombre Comercial', max_length = 30)
    razonsocial = models.CharField('Razón Social', max_length = 30)
    direccion = models.CharField('Dirección', max_length = 30)
    municipio = models.CharField('Municipio', max_length = 30)
    departamento = models.CharField('Departamento', max_length = 30)
    email = models.EmailField('Correo de contacto', max_length = 100)
    telefono = models.CharField('Teléfono de contacto', max_length = 30)
