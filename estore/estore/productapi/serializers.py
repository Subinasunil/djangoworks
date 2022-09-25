from rest_framework import serializers
from productapi.models import Products,Reviews,Carts
from django.contrib.auth.models import User
class Productserializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    category=serializers.CharField()
    price=serializers.IntegerField()
    rating=serializers.FloatField()
    def validate(self,data):
        price=data.get("price")
        if price<0:
            raise serializers.ValidationError("invalid price")
        return data

class ProductModelSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    avg_rating=serializers.CharField(read_only=True)
    review_count=serializers.CharField(read_only=True)
    class Meta:
        model=Products
        fields=[
                "id",
                "name",
                "category",
                "price",
                "avg_rating",
                "review_count"]

class UserSeializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name",
                "last_name",
                "username",
                "email",
                "password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ReviewSerializer(serializers.ModelSerializer):
    author=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"

class CartSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    date=serializers.DateField(read_only=True)
    status=serializers.CharField(read_only=True)
    class Meta:
        model=Carts
        fields=["user",
                "product",
                "date",
                "qty",
                "status"]
    def create(self, validated_data):
        user=self.context.get("user")
        product= self.context.get("product")
        return Carts.objects.create(**validated_data,user=user,product=product)