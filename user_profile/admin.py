from django.contrib import admin
from .models import Profile, ProfileAdmin

# Register your models here.
admin.site.register(Profile, ProfileAdmin)