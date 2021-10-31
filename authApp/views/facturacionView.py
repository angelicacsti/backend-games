from django.conf import settings
from django.http import request
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend

from authApp.models.home import Home
from authApp.models.products import Products
from authApp.models.clients import Clients
from authApp.models.facturacion import Facturacion
from authApp.serializers.facturacionSerializer import FacturacionSerializer

class FacturacionDetailView(generics.RetrieveAPIView):
    queryset           = Facturacion.objects.all()
    serializer_class   = FacturacionSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)

class FacturacionHomeView(generics.ListAPIView):
    queryset           = Facturacion.objects.all()
    serializer_class   = FacturacionSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        queryset = Facturacion.objects.filter(nit_id=self.kwargs['home'])
        return queryset

class FacturacionClientsView(generics.ListAPIView):
    queryset           = Facturacion.objects.all()
    serializer_class   = FacturacionSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        queryset = Facturacion.objects.filter(numerodocumeto_id=self.kwargs['clients'])
        return queryset

class FacturacionProductsView(generics.ListAPIView):
    queryset           = Facturacion.objects.all()
    serializer_class   = FacturacionSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        queryset = Facturacion.objects.filter(codigoproducto_id=self.kwargs['products'])
        return queryset

class FacturacionCreateView(generics.CreateAPIView):
    queryset           = Facturacion.objects.all()
    serializer_class   = FacturacionSerializer
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != int(request.data['user_id']):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        codigoproducto = Products.objects.get(id=request.data['facturacion_data']['codigoproducto'])
        if codigoproducto.unidadesdisponibles < request.data['facturacion_data']['cantidad']:
            stringResponse = {'detail':'Existencias insuficientes'}
            return Response(stringResponse, status=status.HTTP_406_NOT_ACCEPTABLE)
                        
        serializer = FacturacionSerializer(data=request.data['facturacion_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        codigoproducto.unidadesdisponibles -= request.data['facturacion_data']['cantidad']
        codigoproducto.save()

        return Response("Venta creada exitosamente", status=status.HTTP_201_CREATED)

class FacturacionUpdateView(generics.UpdateAPIView):
    queryset           = Facturacion.objects.all()
    serializer_class   = FacturacionSerializer
    permission_classes = (IsAuthenticated,)
    
    def put(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().update(request, *args, **kwargs)


class FacturacionDeleteView(generics.DestroyAPIView):
    queryset           = Facturacion.objects.all()
    serializer_class   = FacturacionSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request, *args, **kwargs)