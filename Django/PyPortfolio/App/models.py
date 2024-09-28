from django.db import models # type: ignore
from ckeditor_uploader.fields import RichTextUploadingField  # type: ignore

# Create your models here.

class About(models.Model):
    section = models.CharField(max_length=80, name='Section')
    key = models.CharField(max_length=100, name='Key')
    value = models.CharField(max_length=1500, name='Value')

    def __str__(self):
        return self.Section + ' | ' + self.Key

class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    avatar = models.FileField()
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name +' | '+ self.designation +' | '+ self.message

class Service(models.Model):
    icon = models.CharField(max_length=50, name='Icon')
    title = models.CharField(max_length=100, name='Title')
    description = RichTextUploadingField() # CKEditor Rich Text Field # models.TextField(name='Description')
    image = models.FileField(upload_to='media/', default='null')

    def __str__(self):
        return self.Title
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=150)
    message = models.TextField() 
