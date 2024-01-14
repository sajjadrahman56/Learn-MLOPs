#from django.http import HttpResponse
from django.shortcuts import render
def homePage(request):
    #return HttpResponse("Hello, This is sajjad !")
    return render(request,'home.html')

def aboutPage(request):
    #return HttpResponse("Sajjad, This is about page !")
    return render(request,'about.html')

def contactPage(request):
    #return HttpResponse("Sajjad, This is contact page !")
    return render(request,'contact.html')
