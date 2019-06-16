from django.shortcuts import render

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")
    
def index_home_function(request):
    return render(request, "base_no_logo.html")
    