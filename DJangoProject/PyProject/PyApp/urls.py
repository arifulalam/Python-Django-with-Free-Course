from django.urls import path # type: ignore
from .views import base, contact

urlpatterns = [
    path('', base, name='base'),
    path('contact-us', contact, name='contact-us')
]