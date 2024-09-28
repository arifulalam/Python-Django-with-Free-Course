from django.contrib import admin # type: ignore
from .models import *

# Register your models here.
admin.site.register(About)
admin.site.register(Testimonial)
admin.site.register(Service)
admin.site.register(Contact)
