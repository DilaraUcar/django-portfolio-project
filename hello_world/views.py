from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import BlogPost

# Create your views here.
class PostList(generic.ListView):
    queryset = BlogPost.objects.filter(status=1).order_by('-created_at')
    template_name = "index.html"

    # Display 10 posts per page
    paginate_by = 5

def post_detail(request, slug):
    """
    Display an individual :model:`hello_world.BlogPost`.

    **Context**

    ``post``
        An instance of :model:`hello_world.BlogPost`.

    **Template:**

    :template:`hello_world/post_detail.html`
    """

    queryset = BlogPost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "hello_world/post_detail.html",
        {"post": post},
    )