from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {'page_title': 'Home'})

def about(request):
    return render(request, 'about.html', {'page_title': 'About'})