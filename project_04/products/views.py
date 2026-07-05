from django.shortcuts import render # A method imported from the shortcuts module in the django package
from django.http import HttpResponse # A class imported from the http module in the django package
from .models import Product

# View functions for the products app; taking HTTP requests to products/ as an input and returning a viewed/rendered resource.
def index(request):
    products = Product.objects.all()  # or .filter(), get(), save(), etc.
    return render(request, 'index.html', {'products': products}) # The context dictionary contains the data to be passed to the index.html template.

def new(request):
    return HttpResponse('New products..')