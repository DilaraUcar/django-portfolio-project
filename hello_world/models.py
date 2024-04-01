from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostBase(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    num_likes = models.IntegerField(default=0)
    is_pinned = models.BooleanField(default=False)

    class Meta:
        abstract = True
