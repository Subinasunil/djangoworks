from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from menuitem.models import menu_items

class Dishesview(APIView):
    def get(self,request,*args,**kwargs):
        all_items=menu_items
        if "category" in request.query_params:
            category=request.query_params.get("category")
            all_items=[item for item in menu_items if item.get("category")==category]
        if "limit" in request.query_params:
            lim=int(request.query_params.get("limit"))
            all_items=all_items[:lim]
        return Response(data=all_items)
class DishDetailview(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        item=[item for item in menu_items if item.get("code")==id].pop()
        return Response(data=item)
    # def put(self,request,*args,**kwargs):
    #     id = kwargs.get("id")
    #     item = [item for item in menu_items if item.get("code") == id].pop()
    #
    #     return Response(data=item)
