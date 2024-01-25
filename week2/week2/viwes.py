from django.http import HttpResponse

def body(request):
    return HttpResponse('hello this is me')