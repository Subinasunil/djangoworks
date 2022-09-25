from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from disheitems.models import Dishes
from disheitems.serializers import Dishserializer,DisheModelserializer
from rest_framework import status
from rest_framework.viewsets import ViewSet
class DishView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        serializer=Dishserializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=Dishserializer(data=request.data)
        if serializer.is_valid():
            Dishes.objects.create(**serializer.validated_data)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class DishDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Dishes.objects.get(id=id)
        serializer=Dishserializer(qs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def put(self,request,*args,**kwargs):
        id = kwargs.get("id")
        instance=Dishes.objects.filter(id=id)
        serializer=Dishserializer(data=request.data)
        if serializer.is_valid():
            # instance.name=serializer.validated_data.get("name")
            # instance.category=serializer.validated_data.get("category")
            # instance.price=serializer.validated_data.get("price")
            # instance.rating=serializer.validated_data.get("rating")
            # instance.save()
            instance.update(**serializer.validated_data)
            return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,*args,**kwargs):
        id = kwargs.get("id")
        instance=Dishes.objects.get(id=id)
        serializer=Dishserializer(instance)
        instance.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)
class DishModelView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        if "category" in request.query_params:
            qs=qs.filter(category__contains=request.query_params.get("category"))
        if "price_gt" in request.query_params:
            qs=qs.filter(price__gte=request.query_params.get("price_gt"))
        serializer=DisheModelserializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=DisheModelserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DishDetailsModelView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Dishes.objects.get(id=id)
        serializer=DisheModelserializer(qs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def put(self,request,*args,**kwargs):
        id =kwargs.get("id")
        object =Dishes.objects.get(id=id)
        serializer =DisheModelserializer(data=request.data,instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        instance =Dishes.objects.get(id=id)
        instance.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_204_NO_CONTENT)

class DishesViewsetView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        seriliazer=DisheModelserializer(qs,many=True)
        return Response(data=seriliazer.data,status=status.HTTP_200_OK)
    def create(self,request,*args,**kwargs):
        serializer=DisheModelserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Dishes.objects.get(id=id)
        serializer=DisheModelserializer(qs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def update(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        qs = Dishes.objects.get(id=id)
        serializer=DisheModelserializer(data=request.data,instance=qs)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Dishes.objects.get(id=id)
        qs.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)
