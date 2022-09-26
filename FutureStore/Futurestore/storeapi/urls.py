from django.urls import path
from storeapi.views import CategoryView,ProductViewsetView,UserModelView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router=DefaultRouter()
router.register("category",CategoryView,basename="category")
router.register("product",ProductViewsetView,basename="product")
router.register("accounts/signup",UserModelView,basename="users")

urlpatterns=[
    path('token',obtain_auth_token),
]+router.urls