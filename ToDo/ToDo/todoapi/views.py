from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from todoapi.serializers import Todoserializer
from todoapp.models import Todos
from rest_framework import authentication,permissions

# Create your views here.

class TodoView(ModelViewSet):
    queryset = Todos.objects.all()
    serializer_class = Todoserializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)
    def create(self, request, *args, **kwargs):
        serializer=Todoserializer(data=request.data,context={"user":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)