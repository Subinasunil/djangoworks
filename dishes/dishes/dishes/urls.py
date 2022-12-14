"""dishes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from disheitems.views import DishView,DishDetailView,DishModelView,DishDetailsModelView,DishesViewsetView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("api/v3/dishes",DishesViewsetView,basename="dishes")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dishes/dishitems',DishView.as_view()),
    path('dishes/dishitems/<int:id>',DishDetailView.as_view()),
    path('api/v2/dishes',DishModelView.as_view()),
    path('api/v2/dishes/<int:id>',DishDetailsModelView.as_view()),
]+router.urls
