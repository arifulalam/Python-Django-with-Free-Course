from django.shortcuts import render # type: ignore
from .models import Service

# Create your views here.

def base(request):
    services = Service.objects.all()
    return render(request, 'index.html', {'services':services})

def contact(request):
    return render(request, 'contact.html')
