from django.contrib import admin
from .models import BlogPost, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('heading', 'slug', 'status', 'created_at')
    search_fields = ['heading']
    list_filter = ('status','created_at',)
    prepopulated_fields = {'slug': ('heading',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)

