from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView
from todoapp import forms
from django.contrib.auth import authenticate,login,logout
from todoapp.models import Todos
from django.contrib import messages
from todoapp.decorators import signin_required
from django.utils.decorators import method_decorator

class SignUpView(CreateView):
    model = Todos
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url =reverse_lazy("signin")
    def form_valid(self, form):
        messages.success(self.request,"Registration successful")
        return super().form_valid(form)


    # def get(self,request,*args,**kwargs):
    #     form=forms.RegistrationForm()
    #     return render(request,"registration.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     form=forms.RegistrationForm(request.POST)
    #     if form.is_valid():
    #         User.objects.create_user(**form.cleaned_data)
    #         messages.success(request,"Registration successful")
    #         return redirect("signin")
    #     else:
    #
    #         return render(request,"registration.html",{"form":form})
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
            if user:
                login(request,user)
                messages.success(request,"Login Success")
                print("login success")
                return redirect("index")
            else:
                messages.error(request,"invalid Username/password")
                print("invalid credentials")
                return render(request,"login.html",{"form":form})
        return render(request, "login.html")
@method_decorator(signin_required,name="dispatch")
class IndexView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["todos"]=Todos.objects.filter(user=self.request.user,status=False)
        return context

    # def get(self, request, *args, **kwargs):
    #     return render(request, "home.html")
@method_decorator(signin_required,name="dispatch")
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
@method_decorator(signin_required,name="dispatch")
class TodoAddView(CreateView):
    model = Todos
    form_class = forms.TodoForm
    template_name = "add-todo.html"
    success_url = reverse_lazy("todo-list")
    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"Todo has been added")
        return super().form_valid(form)

    # def get(self,request,*args,**kwargs):
    #     form=forms.TodoForm()
    #     return render(request,"add-todo.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     form=forms.TodoForm(request.POST)
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #         messages.success(request,"Todo Added")
    #         # Todos.object.create(**form.cleaned_data,data=request.user)
    #         return redirect("index")
    #     else:
    #         messages.error(request,"Adding Failed")
    #         return render(request,"add-todo.html",{"form":form})
@method_decorator(signin_required,name="dispatch")
class TodoListView(ListView):
    model = Todos
    template_name = "todolist.html"
    context_object_name = "todos"
    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)

    # def get(self,request,*args,**kwargs):
    #     all_todos=Todos.objects.filter(user=request.user)
    #     return render(request, "todolist.html",{"todos":all_todos})

@signin_required
def delete_todo(request,*args,**kwargs):
    id=kwargs.get("id")
    Todos.objects.get(id=id).delete()
    messages.success(request,"Todo Deleted")
    return redirect("todo-list")
@method_decorator(signin_required,name="dispatch")
class TodoDetailView(DetailView):
    model = Todos
    template_name = "todo-detail.html"
    context_object_name = "todo"
    pk_url_kwarg = "id"
    # id = kwargs.get("id")
    # todo=Todos.objects.get(id=id)
    # return render(request,"todo-detail.html",{"todo":todo})
@method_decorator(signin_required,name="dispatch")
class TodoEditView(UpdateView):
    model = Todos
    form_class = forms.TodoChangeForm
    template_name = "todo-edit.html"
    success_url = reverse_lazy("todo-list")
    pk_url_kwarg = "id"
    def form_valid(self, form):
        messages.success(self.request,"Todo has been Updated")
        return super().form_valid(form)

    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     todo=Todos.objects.get(id=id)
    #     form=forms.TodoChangeForm(instance=todo)
    #     return render(request,"todo-edit.html",{"form":form})
    #
    # def post(self,request,*args,**kwargs):
    #     id = kwargs.get("id")
    #     todo = Todos.objects.get(id=id)
    #     form=forms.TodoChangeForm(request.POST,instance=todo)
    #     if form.is_valid():
    #         form.save()
    #         msg="todo has been changed"
    #         messages.success(request,msg)
    #         return redirect("todo-list")
    #     else:
    #         msg="todo update failed"
    #         messages.error(request,msg)
    #         return render(request,"todo-edit.html",{"form":form})
