from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm
from django.utils.text import slugify


class PostList(generic.ListView):
    model = BlogPost
    template_name = "index.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = BlogPost.objects.filter(status=1).order_by('-is_pinned', '-created_at')
        query = self.request.GET.get('search')
        if query:
            queryset = queryset.filter(
                Q(heading__icontains=query) |
                Q(content__icontains=query) |
                Q(writer__username__icontains=query)
            )
        self.search_results = queryset.exists()  # Track if there are any results
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogPostForm()
        context['search_term'] = self.request.GET.get('search', '')
        context['no_results'] = not self.search_results and self.request.GET.get('search')
        return context

def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.status = 1  # Set status to Published
            post.slug = slugify(post.heading)  # Generate unique slug based on heading
            post.save()
            messages.success(request, 'Post created successfully.')
            return redirect('post_detail', slug=post.slug)  # Redirect to post_detail with the slug of the newly created post
    else:
        form = BlogPostForm()
    return render(request, 'index.html', {'form': form})

def post_detail(request, slug):
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
                request, messages.SUCCESS, 'Comment submitted successfully'
            )
            print("Comment submitted successfully!")  # Print debugging output
            return HttpResponseRedirect(request.path)  # Redirect to the same URL after successful POST
    else:
        comment_form = CommentForm()  # Form for GET request

    return render(
        request,
        "hello_world/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
    """
    if request.method == "POST":

        queryset = BlogPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.commenter == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
            print("successmessage: Comment deleted successfully!")
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


#@login_required
#def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """
    #queryset = BlogPost.objects.filter(status=1)
    #Blogpost = get_object_or_404(queryset, slug=slug)
    #comment = get_object_or_404(Comment, pk=comment_id)

    #if comment.commenter == request.user:
        #comment.delete()
        #messages.add_message(request, messages.SUCCESS, 'Comment deleted successfully!')
        #print("Comment deleted successfully!")  # Print debugging output
    #else:
        #messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')
        #print("Failed to delete comment: You can only delete your own comments!")  # Print debugging output

    #return HttpResponseRedirect(reverse('post_detail', args=[slug]))


#@login_required
#def post_delete(request, post_id):
    #post = get_object_or_404(BlogPost, id=post_id)

    # Check if the user has permission to delete the post
    #if request.user == post.writer or request.user.is_staff:
        #post.delete()
        #messages.success(request, "Post deleted successfully.")
    #else:
        #messages.error(request, "You don't have permission to delete this post.")
 
    #return redirect('home')  # Redirect to the home page after deletion


@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the user has permission to delete the comment
    if request.user == comment.commenter or request.user.is_staff:
        comment.delete()
        messages.success(request, "Comment deleted successfully.")
    else:
        messages.error(request, "You don't have permission to delete this comment.")

    return redirect(request.META.get('HTTP_REFERER', 'home'))
