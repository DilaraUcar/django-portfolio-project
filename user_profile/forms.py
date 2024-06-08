from .models import Profile
from django import forms
from django_summernote.widgets import SummernoteWidget


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('avatar', 'about',)  # Fields that can be updated
        widgets = {
            #  Accept only image files
            'avatar': forms.FileInput(attrs={'accept': 'image/*'}),
            'about': SummernoteWidget(attrs={"class": "form-control"}),
        }
