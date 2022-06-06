from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request,'index.html')

def forms(request):
    if request.method == "POST":
        album_name = request.POST.get("album_name")
        artist_name = request.POST.get("artist_name")
        album_picture = request.POST.get("album_picture")
        form = forms(album_name=album_name,
        artist_name=artist_name,
        album_picture=album_picture)
        form.save()
        return HttpResponse("Successful")
    return render(request, "forms.html")