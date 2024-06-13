from django import forms
from .models import Comment, BlogPost


class CommentForm(forms.ModelForm):
    """
    Form class for users to commenting and updating on a post
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Comment
        fields = ('content',)


class BlogPostForm(forms.ModelForm):
    """
    Form class for creating a blog posts.
    """
    class Meta:
        """
        Specify the Django model and the fields to include in the form.
        """
        model = BlogPost
        fields = ['heading', 'content']
