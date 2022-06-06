from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request,'index.html')

def toys(request):
    if request.method == "POST":
        toy_name = request.POST.get("toy_name")
        toy_picture = request.POST.get("toy_picture")
        form = toys(toy_name=toy_name,
        toy_picture=toy_picture)
        form.save()
        return HttpResponse("Successful")
    return render(request, "toys.html")