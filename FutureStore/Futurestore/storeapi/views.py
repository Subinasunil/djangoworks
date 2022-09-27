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

class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    # def list(self, request, *args, **kwargs):
    #     id=Categories.objects.get("id")
    #     qs=Product.objects.filter(id=id)
    #     serializer=ProductSerializer(qs,many=True)
    #     return Response(data=serializer.data)

    def get_queryset(self):
        c_id=Categories.objects.get("pk")
        return Product.objects.filter(id=c_id)


class UserModelView(ModelViewSet):
    serializer_class = UserSeializer
    queryset =User.objects.all()
