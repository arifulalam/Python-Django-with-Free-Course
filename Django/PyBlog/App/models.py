from django.db import models # type: ignore

# Import slugify to generate slugs from strings
from django.utils.text import slugify  # type: ignore

from django.utils import timezone # type: ignore

# Create your models here.
class Settings(models.Model):
    key = models.CharField(name='Key', max_length=255)
    value = models.TextField(name='Value')
    createdOn = models.DateTimeField(name='createdOn')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft',   'Draft'),
        ('published',   'Published'),
    )
    title = models.CharField(name='title', max_length=1000)
    slug = models.SlugField(name='slug', unique=True)
    content = models.TextField()
    image = models.FileField(name='Featured Image')
    createdOn = models.DateTimeField(name='createdOn', auto_now_add=True)
    updatedOn = models.DateTimeField(name='updatedOn', auto_now=True)
    publishedOn = models.DateTimeField(name='publishedOn', default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    list_display = ['title', 'slug', 'status', 'createdOn', 'publishedOn', 'updatedOn']
    prepopulated_fields={'slug': ('title',)}
    list_filter=('status', 'createdOn', 'publishedOn')
    search_fields=('title', 'content')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-publishedOn',)
