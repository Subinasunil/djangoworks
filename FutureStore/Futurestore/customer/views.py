from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,ListView,DetailView,UpdateView,FormView
from django.contrib.auth import authenticate,login,logout
from customer import forms
from owner.models import Product,Categories
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
                messages.success(request, "Login Success")
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
class ProductDetailView(DetailView):
    model = Product
    template_name = "product-detail.html"
    context_object_name = "product"
    pk_url_kwarg = "id"