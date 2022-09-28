from rest_framework.serializers import ModelSerializer
from owner.models import Categories,Product,Carts,Reviews
from django.contrib.auth.models import User
from rest_framework import serializers
class CategorySerializer(ModelSerializer):
    class Meta:
        model=Categories
        fields="__all__"
class ProductSerializer(ModelSerializer):
    id=serializers.CharField(read_only=True)
    category=serializers.CharField(read_only=True)
    class Meta:
        model=Product
        fields=[
                "id",
                "Product_name",
                "category",
                "image",
                "price",
                "description"
        ]
    def create(self, validated_data):
       return Product.objects.create(**validated_data)
class UserSeializer(ModelSerializer):
    class Meta:
        model=User
        fields=["first_name",
                "last_name",
                "username",
                "email",
                "password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
class CartSerializer(ModelSerializer):
    product=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Carts
        fields="__all__"
    def create(self,validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Carts.objects.create(**validated_data,user=user,product=product)
class ReviewSerializer(ModelSerializer):
    product = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields= "__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Reviews.objects.create(user=user,product=product,**validated_data)