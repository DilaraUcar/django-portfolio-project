from django import forms
from django_summernote.widgets import SummernoteWidget
from django.core.exceptions import ValidationError

from .models import Profile
import os


class ProfileForm(forms.ModelForm):
    """Form class for users profile to add and update there
    information and avatar, using Django forms.
    """
    class Meta:
        """
        Specify the Django model and fields for the ProfileForm,
        including avatar and about fields.
        """
        model = Profile
        fields = ('avatar', 'about',)  # Fields that can be updated
        widgets = {
            #  Accept only image files
            'avatar': forms.FileInput(attrs={'accept': 'image/*'}),
            'about': SummernoteWidget(attrs={"class": "form-control"}),
        }

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            ext = os.path.splitext(avatar.name)[1].lower()
            valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
            if ext not in valid_extensions:
                raise ValidationError(
                    "Unsupported file. Only .jpg, .jpeg, .png, .gif allowed.")
        return avatar
