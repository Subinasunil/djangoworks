from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"u must login")
            return redirect("sigin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

def sign_as_user(fn):
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return redirect("index")
        elif User:
            return redirect("userpage")
        else:
            return fn(request, *args, **kwargs)
    return wrapper
