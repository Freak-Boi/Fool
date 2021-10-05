from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse("this is about us dude")


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
