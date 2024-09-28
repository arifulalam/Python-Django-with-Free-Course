from django.urls import path # type: ignore
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact-us', contact, name='contact'),
    path('about-us', about, name='about'),
    path('portfolio', portfolio, name='portfolio'),
    path('portfolio-details', portfolio_details, name='portfolio-details'),
    path('resume', resume, name='resume'),
    path('servicess', services, name='services'),
    path('service/<int:pk>', service_details, name='service'),
]