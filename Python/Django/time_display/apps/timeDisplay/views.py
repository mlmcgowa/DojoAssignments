from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.

def index(request):
    context = {
        "time": strftime("%H:%M %p %Y-%m-%d ", gmtime())
    }
    return render(request, 'timeDisplay/index.html', context)
