from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,ListView,DetailView,UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from bookapi import forms
from bookapi.models import Books
from django.contrib import messages
from bookapi.decorators import signin_required
from django.utils.decorators import method_decorator



# Create your views here.


class SignUpView(CreateView):
    model = Books
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url =reverse_lazy("signin")
    def form_valid(self, form):
        messages.success(self.request,"Registration successful")
        return super().form_valid(form)

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form = forms.LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if request.user.is_superuser:
                login(request, user)
                messages.success(request, "Login Success")
                print("login success")
                return redirect("index")
            elif user:
                login(request, user)
                messages.success(request, "Login Success")
                print("login success")
                return redirect("userpage")
            else:
                messages.error(request,"invalid Username/password")
                print("invalid credentials")
                return render(request,"login.html",{"form":form})
        return render(request, "login.html")
@method_decorator(signin_required,name="dispatch")
class IndexView(TemplateView):
    template_name = "home.html"

@method_decorator(signin_required,name="dispatch")
class UserPageView(TemplateView):
    template_name = "userpage.html"
@method_decorator(signin_required,name="dispatch")
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")

@method_decorator(signin_required,name="dispatch")
class BookAddView(CreateView):
    model = Books
    form_class = forms.BookForm
    template_name = "add-book.html"
    success_url = reverse_lazy("listbook")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Book has been added")
        return super().form_valid(form)


@method_decorator(signin_required,name="dispatch")
class BookListView(ListView):
    model = Books
    template_name = "list-book.html"
    context_object_name = "books"
    def get_queryset(self):
        return Books.objects.all()



@signin_required
def delete_book(request,*args,**kwargs):
    id=kwargs.get("id")
    Books.objects.get(id=id).delete()
    messages.success(request,"Book Deleted")
    return redirect("listbook")

@method_decorator(signin_required,name="dispatch")
class TodoDetailView(DetailView):
    model = Books
    template_name = "book-detail.html"
    context_object_name = "book"
    pk_url_kwarg = "id"

@method_decorator(signin_required,name="dispatch")
class BookEditView(UpdateView):
    model = Books
    form_class = forms.BookEditForm
    template_name = "book-edit.html"
    success_url = reverse_lazy("listbook")
    pk_url_kwarg = "id"
    def form_valid(self, form):
        messages.success(self.request,"Book has been Updated")
        return super().form_valid(form)