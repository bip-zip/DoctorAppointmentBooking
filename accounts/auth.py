from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function

def admin_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff and request.user.is_superuser:
            return redirect('/admin')
        else:
           return view_function(request, *args, **kwargs)
    return wrapper_function

def doctor_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff :
            return view_function(request, *args, **kwargs)
        else:
            return redirect('mainapp:home')
    return wrapper_function

def user_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return redirect('doctorsapp:doctorhome')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function




