from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from .models import BlogPost, Comment
from .forms import CommentForm


class PostListTestCase(TestCase):
    """
    Base test class for testing views related to blog posts and comments.
    """
    def setUp(self):
        """Create a superuser and a blog post"""
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com")
        self.post = BlogPost.objects.create(
            heading='Test Post',
            content='This is test content.',
            writer=self.user,
            status=1,
            slug=slugify('Test Post')
        )

    def test_render_post_detail_page_with_comment_form(self):
        """Verifies a single blog post containing a comment form is returned"""
        response = self.client.get(
            reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.post.heading.encode(), response.content)
        self.assertIn(self.post.content.encode(), response.content)
        self.assertIsInstance(response.context['comment_form'], CommentForm)

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(username="myUsername", password="myPassword")
        post_data = {'content': 'This is a test comment.'}
        response = self.client.post(
            reverse('post_detail', args=[self.post.slug]), post_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            self.post.comments.filter(content=post_data['content']).exists())

    def test_search_by_heading(self):
        """
        Test searching for posts by heading.
        """
        response = self.client.get(reverse('home') + '?search=Test')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_search_by_content(self):
        """
        Test searching for posts by content.
        """
        response = self.client.get(reverse('home') + '?search=test content')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_search_by_writer(self):
        """
        Test searching for posts by writer username.
        """
        response = self.client.get(reverse('home') + '?search=myUsername')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_no_search_results(self):
        """
        Test searching with no results found.
        """
        response = self.client.get(reverse('home') + '?search=Nonexistent')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Test Post')
        self.assertContains(
            response, 'No search results found. Please try again.')

    def test_comment_edit(self):
        """
        Test editing a comment on a post.
        """
        comment = Comment.objects.create(
            commenter=self.user,
            blog_post=self.post,
            content='Initial comment content.')
        self.client.login(username='myUsername', password='myPassword')
        post_data = {'content': 'Updated comment content.'}
        response = self.client.post(
            reverse('comment_edit', args=[self.post.slug, comment.id]),
            post_data)
        self.assertEqual(response.status_code, 302)
        edited_comment = Comment.objects.get(pk=comment.id)
        self.assertEqual(edited_comment.content, 'Updated comment content.')

    def test_comment_delete(self):
        """
        Test deleting a comment on a post.
        """
        comment = Comment.objects.create(
            commenter=self.user,
            blog_post=self.post,
            content='Comment to be deleted.')
        self.client.login(username='myUsername', password='myPassword')
        response = self.client.post(
            reverse('delete_comment', args=[comment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(pk=comment.id).exists())
