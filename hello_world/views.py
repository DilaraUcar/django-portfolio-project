from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import BlogPost
from .forms import CommentForm

# Create your views here.
class PostList(generic.ListView):
    queryset = BlogPost.objects.filter(status=1).order_by('-created_at')
    template_name = "index.html"

    # Display 5 posts per page
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
    comments = post.comments.all().order_by("created_at")
    comment_count = post.comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commenter = request.user
            comment.blog_post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, 'Comment submitted successfully'
            )
            comment_form = CommentForm()  # Reset form after successful submission
    else:
        comment_form = CommentForm()  # Form for GET request


    return render(
        request,
        "hello_world/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },   
    )