from django.shortcuts import render

# week2/yourapp/views.py
from django.shortcuts import render
from django.http import HttpResponse

def homnew1(request):
    return  HttpResponse("Hello, world. You're at the polls index.")

 
