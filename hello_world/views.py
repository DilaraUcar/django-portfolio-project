from django.shortcuts import render
from django.views import generic
from .models import BlogPost

# Create your views here.
class PostList(generic.ListView):
    queryset = BlogPost.objects.all()
    template_name = "post_details.html"