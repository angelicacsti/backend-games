from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('register/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('home/<int:user>/<int:pk>/', views.HomeDetailView.as_view()),
    path('home/create/', views.HomeCreateView.as_view()), 
    path('home/update/<int:user>/<int:pk>/', views.HomeUpdateView.as_view()), 
    path('products/<int:user>/<int:pk>/', views.ProductsDetailView.as_view()), 
    path('products/create/',  views.ProductsCreateView.as_view()),
    path('products/update/<int:user>/<int:pk>/', views.ProductsUpdateView.as_view()),
    path('products/delete/<int:user>/<int:pk>/', views.ProductsUpdateView.as_view()),
    path('clients/<int:user>/<int:pk>/', views.ClientsDetailView.as_view()), 
    path('clients/create/',  views.ClientsCreateView.as_view()),
    path('clients/update/<int:user>/<int:pk>/', views.ClientsUpdateView.as_view()),
    path('clients/delete/<int:user>/<int:pk>/', views.ClientsUpdateView.as_view()),
    path('facturacion/<int:user>/<int:pk>/', views.FacturacionDetailView.as_view()), 
    path('facturacion/create/',  views.FacturacionCreateView.as_view()),
    path('facturacion/update/<int:user>/<int:pk>/', views.FacturacionUpdateView.as_view()),
    path('facturacion/delete/<int:user>/<int:pk>/', views.FacturacionUpdateView.as_view()),

]
