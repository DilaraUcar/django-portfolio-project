from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class ProfileViewTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="test_user",
            password="hejsan123!"
        )

    def test_get_profile_page(self):
        """Test that the profile page is accessible"""
        response = self.client.get(f"/profile/{self.user.username}/")
        self.assertEqual(response.status_code, 200)

    def test_post_delete_account(self):
        """Test account deletion via POST request"""
        self.client.force_login(self.user)
        response = self.client.post(reverse("delete_account"))
        self.assertRedirects(response, reverse("home"))
        self.assertFalse(
            User.objects.filter(username=self.user.username).exists())
