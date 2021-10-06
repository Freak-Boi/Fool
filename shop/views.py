from django.shortcuts import render
from .models import Product
# Create your views here.
from django.http import HttpResponse
from math import ceil


# Create your views here.


def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nslides = n//4 + ceil((n/4)-(n//4))
    params = {'no._of_slides':nslides, 'range': range(1, nslides), 'product': products}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("you can contact with us here")


def tracker(request):
    return HttpResponse("throught this you can trak everything")


def search(request):
    return HttpResponse("here u can search")


def productview(request):
    return HttpResponse("the product view is here")


def checkout(request):
    return HttpResponse("the checkout function is available here")
