from django.http import HttpResponse
from django.shortcuts import render

def homepage34(request):  
    return render(request, 'index.html')

def body(request):
    return HttpResponse('hello this is me body')

def bo(request):
    return HttpResponse('hello this is bo sa bo')