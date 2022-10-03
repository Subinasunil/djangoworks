from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,ListView,DetailView,UpdateView,FormView
from django.contrib.auth import authenticate,login,logout
from customer import forms
from owner.models import Product,Categories,Carts,Order
from django.contrib import messages

# Create your views here.

class RegistrationView(CreateView):
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url =reverse_lazy("login")
    def form_valid(self, form):
        messages.success(self.request,"Registration successful")
        return super().form_valid(form)

class LoginView(FormView):
    template_name = "login.html"
    form_class = forms.LoginForm

    def post(self,request,*args,**kwargs):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if request.user.is_superuser:
                    return redirect("dashboard")
                    messages.success(request, "Login Success")
                else:
                    return redirect("home")
        else:
            messages.error(request, "invalid Username/password")
            return render(request, "login.html", {"form": form})
class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        all_products=Product.objects.all()
        context["products"]=all_products
        return context
class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")
class ProductDetailView(DetailView):
    model = Product
    template_name = "product-detail.html"
    context_object_name = "product"
    pk_url_kwarg = "id"

class Addcart(FormView):
    template_name = "add-cart.html"
    form_class = forms.AddCartForm
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        product=Product.objects.get(id=id)
        return render(request,self.template_name,{"form":forms.AddCartForm(),"product":product})
    def post(self,request,*args,**kwargs):
        id = kwargs.get("id")
        product = Product.objects.get(id=id)
        qty=request.POST.get("qty")
        user=request.user
        Carts.objects.create(product=product,
                             user=user,
                             qty=qty)
        return redirect("home")

class MycartView(ListView):
    model=Carts
    template_name = "cart-list.html"
    context_object_name = "carts"

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user).exclude(status="cancelled").order_by("-created_date")

class CartRemoveView(ListView):
    model = Carts
    template_name = "cart-remove.html"
    # context_object_name = "carts"

    # def get_queryset(self):
    #     # id=self.kwargs.get("pk")
    #     # Carts.objects.get(id=id).delete()
    #     return Carts.objects.filter(user=self.request.user).exclude(status="cancelled")
    def post(self,request,*args,**kwargs):
        cart_id = kwargs.get("cid")
        product_id = kwargs.get("pid")
        cart = Carts.objects.get(id=cart_id)
        product = Product.objects.get(id=product_id)
        cart.delete()
        cart.status="cancelled"
        return redirect("home")



class PlaceOrderView(FormView):
    template_name = "place-order.html"
    form_class = forms.OrderForm

    def post(self, request, *args, **kwargs):
        cart_id=kwargs.get("cid")
        product_id=kwargs.get("pid")
        cart=Carts.objects.get(id=cart_id)
        product=Product.objects.get(id=product_id)
        user=request.user
        delivery_address=request.POST.get("delivery_address")
        Order.objects.create(product=product,
                             user=user,
                             delivery_address=delivery_address)
        cart.status="order-placed"
        cart.save()
        return redirect("home")



