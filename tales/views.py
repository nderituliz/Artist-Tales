from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image
import datetime as dt

def photos(request):
    photos = Image.objects.all()

    return render(request,'index.html',{'photos':photos})

def location(request, location):
    location = Image.objects.get(id=photo_id)

    return render(request,'photo.html',{'location':location})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Image.search_by_category(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {"message":message, "photos": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})