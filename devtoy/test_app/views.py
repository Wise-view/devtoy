import re
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
#I'll create a view called homepage.
def homepage(request):
    return HttpResponse("Hello <strong>Wise View<strong/>")
