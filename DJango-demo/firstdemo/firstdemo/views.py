from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello this is Sajjad World")

def about(request):
    return HttpResponse("This is my about page")

def sr56(request):
    return HttpResponse('sajjadrahman56')