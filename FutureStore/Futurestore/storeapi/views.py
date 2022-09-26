from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from storeapi.serializers import CategorySerializer,ProductSerializer,UserSeializer
from owner.models import Categories,Product
from rest_framework import authentication,permissions
from django.contrib.auth.models import User

# Create your views here.

class CategoryView(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ProductViewsetView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class UserModelView(ModelViewSet):
    serializer_class = UserSeializer
    queryset =User.objects.all()
