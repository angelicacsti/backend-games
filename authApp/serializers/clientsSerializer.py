from authApp.models.clients import Clients
from rest_framework import serializers


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Clients
        fields = ["numerodocumento", "nombrecompleto", "direccion", "municipio", "departamento", "correocontacto", "telefonocontacto"]

    def to_representation(self, obj):
        clients = Clients.objects.get(id=obj.id)
        return {
            'id' : clients.id,
            'numerodocumento' : clients.numerodocumento, 
            'nombrecompleto' : clients.nombrecompleto, 
            'direccion' : clients.direccion,
            'municipio' : clients.municipio,
            'departamento' : clients.departamento,
            'correocontacto' : clients.correocontacto,
            'telefonocontacto' : clients.telefonocontacto
        }