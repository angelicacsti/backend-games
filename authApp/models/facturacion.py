from django.db import models
from .home import Home
from .clients import Clients
from .products import Products

class Facturacion(models.Model):
    id = models.AutoField(primary_key=True)
    fechaemision = models.DateField(auto_now_add=True, blank=True)
    mediodepago = models.CharField(max_length=100)
    nit = models.ForeignKey(Home, related_name="nit_home", on_delete=models.CASCADE)
    numerodocumento = models.ForeignKey(Clients, related_name="personalid_clients", on_delete=models.CASCADE)
    codigoproducto = models.ForeignKey(Products, related_name="codeproduct_products", on_delete=models.CASCADE)
    # descripcion = models.ForeignKey(Products, related_name="descripcion_products", on_delete=models.CASCADE)
    # precio = models.ForeignKey(Products, related_name="precio_products", on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    iva = models.IntegerField(default=16)
    montoiva = models.IntegerField(default=0)
    totalitem = models.IntegerField(default=0)
    subtotal = models.IntegerField(default=0)
    totaliva = models.IntegerField(default=0)
    totalmasimpuestos = models.IntegerField(default=0)
    totaloperacion = models.IntegerField(default=0)
