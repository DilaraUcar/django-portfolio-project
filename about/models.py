from django.db import models


# Create your models here.
class About(models.Model):
    """
    Stores a single about me text
    """
    heading = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.heading
