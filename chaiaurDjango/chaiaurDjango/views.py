
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello World, You are at Home Page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello World, You are at about Page")

def contact(request):
    return HttpResponse("Hello World, You are at Contact Page")


