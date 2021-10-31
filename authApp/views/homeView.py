from django.conf import settings
from django.http import request
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend

from authApp.models.home import Home
from authApp.serializers.homeSerializer import HomeSerializer

class HomeDetailView(generics.RetrieveAPIView):
    queryset           = Home.objects.all()
    serializer_class   = HomeSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)

class HomeCreateView(generics.CreateAPIView):
    queryset           = Home.objects.all()
    serializer_class   = HomeSerializer
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != int(request.data['user_id']):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        serializer = HomeSerializer(data=request.data['home_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Información ingresada correctamente", status=status.HTTP_201_CREATED)
        
class HomeUpdateView(generics.UpdateAPIView):
    queryset           = Home.objects.all()
    serializer_class   = HomeSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().update(request, *args, **kwargs)