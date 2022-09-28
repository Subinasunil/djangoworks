from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from storeapi.serializers import CategorySerializer,ProductSerializer,UserSeializer,CartSerializer,ReviewSerializer
from owner.models import Categories,Product,Carts,Reviews
from rest_framework import authentication,permissions
from django.contrib.auth.models import User
from rest_framework.decorators import action

# Create your views here.

class CategoryView(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    @action(methods=["get"], detail=True)
    def get_products(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        category =Categories.objects.get(id=id)
        product=category.product_set.all()
        serializer=ProductSerializer(product,many=True)
        return Response(data=serializer.data)
class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    @action(methods=["post"], detail=True)
    def add_to_cart(self, request, *args, **kwargs):
        user = request.user
        id = kwargs.get("pk")
        product = Product.objects.get(id=id)
        serializer = CartSerializer(data=request.data, context={"user": user, "product": product})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    @action(methods=["post"], detail=True)
    def add_review(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        product = Product.objects.get(id=id)
        user = request.user
        serializer = ReviewSerializer(data=request.data, context={"user": user, "product": product})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    @action(methods=["get"], detail=True)
    def get_review(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        product = Product.objects.get(id=id)
        reviews = product.reviews_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)


class UserModelView(ModelViewSet):
    serializer_class = UserSeializer
    queryset =User.objects.all()

class CartsView(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Carts.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

