from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Base model to be used in other models
class PostBase(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    num_likes = models.IntegerField(default=0)
    is_pinned = models.BooleanField(default=False)

    class Meta:
        abstract = True


STATUS = ((0, "Draft"), (1, "Published"))

class BlogPost(PostBase):
    heading = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="authored_posts"
    )
    class Meta:
        ordering = ["-created_at"]

    def get_url(self):
        return reverse("post_detail", args=[str(self.slug)])

    def __str__(self):
        return f"{self.heading} | by {self.writer}"

    status = models.IntegerField(choices=STATUS, default=0)


class Comment(PostBase):
    commenter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commented_posts"
    )
    blog_post = models.ForeignKey(
            BlogPost, on_delete=models.CASCADE, related_name="comments"
    )

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment: {self.content} | by {self.commenter}"
