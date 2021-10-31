from authApp.models.home import Home
from rest_framework import serializers


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Home
        fields = ["nit", "nombrecomercial", "razonsocial", "direccion", "municipio", "departamento", "email", "telefono"]

    def to_representation(self, obj):
        home = Home.objects.get(id=obj.id)
        return {
            'id' : home.id,
            'nit' : home.nit, 
            'nombrecomercial' : home.nombrecomercial, 
            'razonsocial' : home.razonsocial,
            'direccion' : home.direccion,
            'municipio' : home.municipio,
            'departamento' : home.departamento,
            'email' : home.email,
            'telefono' : home.telefono
        }