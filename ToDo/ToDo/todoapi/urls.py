from django.urls import path
from todoapi.views import TodoView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("todos",TodoView,basename="todos")

urlpatterns=[

]+router.urls