from django.shortcuts import render
from django.views import generic
from .models import BlogPost

# Create your views here.
class PostList(generic.ListView):
    queryset = BlogPost.objects.filter(status=1).order_by('-created_at')
    template_name = "index.html"
    paginate_by = 10