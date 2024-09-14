from django.http import HttpResponse
from django.shortcuts import render
from .models import About, Testimonial, Service, Contact

global socials
socials = About.objects.filter(Section = 'Socials')

# Create your views here.
def index(request):    
    name = About.objects.filter(Section = 'About', Key = 'Name').values()[0]['Value']
    professions = About.objects.filter(Section = 'About', Key = 'professions').values()[0]['Value']
    profession = professions.split(',')[0]
    return render(request, 'index.html', {
        'page_title': 'Home', 
        'socials': socials, 
        'name': name, 
        'professions': professions, 
        'profession': profession
    })

def contact(request):
    form_data = request.POST
    
    #global message
    message = None
    
    if request.POST:
        _contact = Contact.objects.create(
            name = request.POST['name'], 
            email = request.POST['email'], 
            subject = request.POST['subject'], 
            message = request.POST['message']
        )
        
        if(_contact.name != ''):
            message = {'class':'sent-message', 'message': 'Your message has been sent. Thank you!'}
        else:
            message = {'class':'error-message', 'message': 'Your message sending failed. Try again later.'}
            
    return render(request, 'contact.html', {'page_title': 'Contact Us', 'socials': socials, 'message': message})

def about(request):
    about = About.objects.all()
    title = about.filter(Section = 'About', Key = 'Title').values()[0]['Value']
    subtitle = about.filter(Section = 'About', Key = 'subtitle').values()[0]['Value']
    about = {
        'Birthday': about.filter(Section = 'About', Key = 'Birthday').values()[0]['Value'],
        'Age': about.filter(Section = 'About', Key = 'Age').values()[0]['Value'],
        'Website': about.filter(Section = 'About', Key = 'Website').values()[0]['Value'],
        'Degree': about.filter(Section = 'About', Key = 'Degree').values()[0]['Value'],
        'Phone': about.filter(Section = 'About', Key = 'Phone').values()[0]['Value'],
        'Email': about.filter(Section = 'About', Key = 'Email').values()[0]['Value'],
        'City': about.filter(Section = 'About', Key = 'City').values()[0]['Value'],
        'Hometown': about.filter(Section = 'About', Key = 'Hometown').values()[0]['Value'],
        'Description': about.filter(Section = 'About', Key = 'Description').values()[0]['Value'],
    }
    skills = About.objects.filter(Section = 'Skills')
    interests = About.objects.filter(Section = 'Interests')
    testimonials = Testimonial.objects.all()
    return render(request, 'about.html', {
        'page_title': 'About Us', 
        'title': title, 
        'subtitle': subtitle, 
        'about': about, 
        'skills': skills,
        'interests': interests,
        'testimonials': testimonials,
        'socials': socials,
    })

def portfolio(request):
    return render(request, 'portfolio.html', {'page_title': 'Portfolio', 'socials': socials})

def portfolio_details(request):
    return render(request, 'portfolio-details.html', {'page_title': 'Portfolio Details', 'socials': socials})

def resume(request):
    return render(request, 'resume.html', {'page_title': 'Resume', 'socials': socials})

def services(request):
    services = Service.objects.all()
    print(services)
    return render(request, 'services.html', {'page_title': 'Services', 'socials': socials, 'services': services})

def service_details(request, pk):
    service = Service.objects.get(pk = pk)
    return render(request, 'service-details.html', {'page_title': 'Service Details', 'socials': socials, 'service': service})
