from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost, Comment


@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('heading', 'slug', 'status', 'created_at')
    search_fields = ['heading']
    list_filter = ('status', 'created_at',)
    prepopulated_fields = {'slug': ('heading',)}
    summernote_fields = ('content',)


admin.site.register(Comment)
