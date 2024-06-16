from django.test import TestCase
from .forms import BlogPostForm, CommentForm


class TestPostForm(TestCase):
    """
    Test the validity of BlogPostForm.

    This test case checks whether the BlogPostForm validates correctly
    with given input data.
    """
    def test_form_is_valid(self):

        post_form = BlogPostForm({'heading': 'This is a great post', 'content': 'This is a test.'})
        self.assertTrue(post_form.is_valid())

    def test_form_is_invalid(self):
        post_form = BlogPostForm({'heading': '', 'content': ''})
        self.assertFalse(post_form.is_valid(), msg="Form is valid")


class TestCommentForm(TestCase):
    """
    Test the validity of CommentForm.

    This test case checks whether the CommentForm validates correctly
    with given input data.
    """
    def test_form_is_valid(self):

        comment_form = CommentForm({'content': 'This is a test.'})
        self.assertTrue(comment_form.is_valid())

    def test_form_is_invalid(self):
        comment_form = CommentForm({'content': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")
