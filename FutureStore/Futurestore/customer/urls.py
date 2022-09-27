from django.urls import path
from customer import views

urlpatterns = [
    path('register', views.RegistrationView.as_view(), name="register"),
    path("", views.LoginView.as_view(), name="login"),
    path("home", views.HomeView.as_view(), name="home"),
    path("product/<int:id>", views.ProductDetailView.as_view(), name="product-detail"),
    ]