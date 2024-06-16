from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from django.test import TestCase
from .forms import ProfileForm


class ProfileFormTests(TestCase):
    """
    Test the validity of ProfileForm.

    This test case checks whether the ProfileForm validates correctly
    with given input data, including file uploads.
    """
    def test_valid_avatar_file(self):
        valid_image = SimpleUploadedFile(
            "valid_image.jpg", b"file_content", content_type="image/jpeg")
        form_data = {'avatar': valid_image, 'about': 'Valid about text', }
        form = ProfileForm(data=form_data, files=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_avatar_file(self):
        invalid_file = SimpleUploadedFile(
            "invalid_file.txt", b"file_content", content_type="text/plain")
        form_data = {'avatar': invalid_file, 'about': 'Invalid about text', }
        form = ProfileForm(data=form_data, files=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('avatar', form.errors)  # Check if 'avatar' has errors
        self.assertEqual(
            form.errors['avatar'],
            ["Unsupported file. Only .jpg, .jpeg, .png, .gif allowed."])
