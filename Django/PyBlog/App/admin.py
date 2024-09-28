from django.contrib import admin # type: ignore
from .models import *

from django_summernote.admin import SummernoteModelAdmin # type: ignore

# Register your models here.
admin.site.register(Settings)

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

    list_display=('title', 'slug', 'publishedOn', 'status')
    list_filter=('status', 'createdOn', 'publishedOn', 'updatedOn')
    search_fields=('title', 'content')
    prepopulated_fields={'slug': ('title',)}
    # raw_id_fields=('author',)
    date_hierarchy='publishedOn'