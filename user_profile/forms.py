from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Profile


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
