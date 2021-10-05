from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def boi(request):
    # with open()
    return render(request, 'blog/boi.html')

