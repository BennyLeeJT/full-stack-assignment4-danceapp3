from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from .forms import loginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == "POST":
        username_var = request.POST.get("username")
        password_var = request.POST.get("password")
        user = auth.authenticate(username=username_var, password=password_var)
    else:
        login_form = loginForm()
        return render(request, "login.html",
        {
            "form_selfname" : login_form
        })



def logout(request):
    auth.logout(request)
    return redirect(index)

@login_required
def vip_view_function(request):
    return HttpResponse("For logged in user only")
