from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from django.utils.text import slugify

from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm


class PostList(generic.ListView):
    """
    Returns all published posts in :model:`hello_world.BlogPost`
    and displays them in a page of five posts.

    **Context**

    ``model``
        Model class for which this view is displaying objects (BlogPost).
    ``template_name``
        Template used to render the list of blog posts ("index.html").
    ``paginate_by``
        Number of blog posts per page.

    **Methods**

    ``get_queryset``
        Retrieves the queryset of published blog posts filtered by
        status and search query.
    ``get_context_data``
        Adds additional context data for rendering the template,
        including form and search results.

    **Template:**

    :template:`index.html`
    """
    model = BlogPost
    template_name = "index.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = (
            BlogPost.objects
            .filter(status=1)
            .order_by('-is_pinned', '-created_at')
            )
        query = self.request.GET.get('search')
        if query:
            queryset = queryset.filter(
                Q(heading__icontains=query) |
                Q(content__icontains=query) |
                Q(writer__username__icontains=query)
            )
        self.search_results = queryset.exists()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogPostForm()
        context['search_term'] = self.request.GET.get('search', '')
        no_results = not self.search_results and self.request.GET.get('search')
        context['no_results'] = no_results
        return context


def create_post(request):
    """
    Creates a new blog post based on user input.

    **Context**

    ``request``
        HTTP request object containing form data.

    **Template:**

    :template:`index.html`
    """
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.status = 1  # Set status to Published
            post.slug = slugify(post.heading)

            # Check for uniqueness of the slug
            if BlogPost.objects.filter(slug=post.slug).exists():
                return render(request, 'index.html', {'form': form})

            post.save()
            messages.success(request, 'Post created successfully.')
            return redirect('post_detail', slug=post.slug)
        else:
            messages.error(
                request, 'A post with this title already exists. Please retry.'
            )
            return redirect(reverse('home'))
    else:
        form = BlogPostForm()

    return render(request, 'index.html', {'form': form})


def post_detail(request, slug):
    """
    Displays detailed information about a specific blog post.

    **Context**

    ``request``
        HTTP request object containing form data.
    ``slug``
        Unique slug identifying the blog post.

    **Template:**

    :template:`hello_world/post_detail.html`
    """
    post = get_object_or_404(BlogPost.objects.filter(status=1), slug=slug)
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
                request, messages.SUCCESS, 'Comment submitted successfully')
            return HttpResponseRedirect(request.path)
    else:
        comment_form = CommentForm()  # Form for GET request

    # Create a form for each comment
    edit_comment_forms = {
        comment.id: CommentForm(instance=comment)
        for comment in comments
        }

    return render(
        request,
        "hello_world/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "edit_comment_forms": edit_comment_forms,
        }
    )


@login_required
def comment_edit(request, slug, comment_id):
    """
    Edits an existing comment on a blog post.

    **Context**

    ``request``
        HTTP request object containing form data.
    ``slug``
        Unique slug identifying the blog post.
    ``comment_id``
        Primary key of the comment to be edited.

    **Template:**

    :template:`hello_world/post_detail.html`
    """
    if request.method == "POST":
        queryset = BlogPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.commenter == request.user:
            comment_form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Comment updated successfully!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`hello_world.BlogPost`.
    ``comment``
        A single comment related to the post.
    """
    queryset = BlogPost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.commenter == request.user:
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Comment deleted successfully!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
