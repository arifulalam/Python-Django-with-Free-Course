from django.urls import path
from .views import index, contact, about, portfolio, portfolio_details, resume, services, service_details

urlpatterns = [
    path('', index, name = 'index'),
    path('contact-us', contact, name = 'contact'),
    path('about-us', about, name = 'about'),
    path('services', services, name = 'services'),
    path('service-details/<int:pk>', service_details, name = 'service_details'),
    path('portfolio', portfolio, name = 'portfolio'),
    path('portfolio-details', portfolio_details, name = 'portfolio_details'),
    path('resume', resume, name = 'resume'),
]