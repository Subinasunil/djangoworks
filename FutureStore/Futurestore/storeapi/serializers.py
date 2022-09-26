from rest_framework.serializers import ModelSerializer
from owner.models import Categories,Product
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
