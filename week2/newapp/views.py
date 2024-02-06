from django.shortcuts import render

# week2/yourapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def homnew1(request):
    return  HttpResponse("Hello, world. You're at the polls index.")

def homnew11(request):
    template = loader.get_template('my.html')
    return HttpResponse(template.render())
