from .models import Comment, BlogPost
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['heading', 'content']
