from authApp.models.products import Products
from rest_framework import serializers

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Products
        fields = ["codigoproducto", "categoriaproducto", "descripcion", "genero", "precio", "unidadesdisponibles"]

    def to_representation(self, obj):
            products = Products.objects.get(id=obj.id)
            return {
                'id' : products.id,
                'codigoproducto' : products.codigoproducto, 
                'categoriaproducto' : products.categoriaproducto, 
                'descripcion' : products.descripcion,
                'genero' : products.genero,
                'precio' : products.precio,
                'unidadesdisponibles' : products.unidadesdisponibles
            }