from django.urls import path
from storeapi.views import CategoryView,ProductView,UserModelView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router=DefaultRouter()
router.register("category",CategoryView,basename="category")
router.register("accounts/signup",UserModelView,basename="users")
router.register("product",ProductView,basename="product")
router.register("cart",CategoryView,basename="cart")

urlpatterns=[
    path('token',obtain_auth_token),
]+router.urls