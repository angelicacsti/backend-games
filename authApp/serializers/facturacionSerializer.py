from authApp.models.home import Home
from authApp.models.clients import Clients
from authApp.models.products import Products
from authApp.models.facturacion import Facturacion
from rest_framework import serializers

class FacturacionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Facturacion
        fields = ["fechaemision", "mediodepago", "cantidad", "iva", "montoiva", "totalitem", "subtotal", "totaliva", "totalmasimpuestos", "totaloperacion", "nit", "numerodocumento", "codigoproducto"]

        def to_representation(self, obj):
            facturacion = Facturacion.objects.get(id=obj.id)
            nit  = Home.objects.get(id=facturacion.nit_id)
            numerodocumento = Clients.objects.get(id=facturacion.numerodocumento_id)
            codigoproducto = Products.objects.get(id=facturacion.codigoproducto_id)
            return{
                'idventa' : facturacion.idventa,
                'fechaemision' : facturacion.fechaemision,
                'mediodepago' : facturacion.mediodepago,
                'cantidad' : facturacion.cantidad,
                'iva' : facturacion.iva,
                'montoiva' : facturacion.montoiva,
                'totalitem' : facturacion.totalitem,
                'subtotal' : facturacion.subtotal,
                'totaliva' : facturacion.totaliva,
                'totalmasimpuestos' : facturacion.totalmasimpuestos,
                'totaloperacion' : facturacion.totaloperacion, 
                'nit' : {
                    'nombrecomercial' : nit.nombrecomercial, 
                    'razonsocial' : nit.razonsocial,
                    'direccion' : nit.direccion,
                    'municipio' : nit.municipio,
                    'departamento' : nit.departamento,
                    'email' : nit.email,
                    'telefono' : nit.telefono

                },
                'numerodocumento' : {
                   'nombrecompleto' : numerodocumento.nombrecompleto, 
                   'direccion' : numerodocumento.direccion,
                   'municipio' : numerodocumento.municipio,
                   'departamento' : numerodocumento.departamento,
                   'correocontacto' : numerodocumento.correocontacto,
                   'telefonocontacto' : numerodocumento.telefonocontacto
                },
                'codigoproducto': { 
                    'descripcion' : codigoproducto.descripcion,
                    'precio' : codigoproducto.precio
                }
            }