from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    linkabout='Rango says hey there partner!:<a href="/rango/about/">About</a>'
    return HttpResponse(linkabout)


def about(request):
    linkindex='Rango says here is the about page.:<a href="/rango/">Index</a>'
    return HttpResponse(linkindex)