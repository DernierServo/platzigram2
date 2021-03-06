""" Posts models."""

# Django
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """Post models"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #profile = models.ForeignKey('Profile', on_delete=models.CASCADE)   # Esto sería importando el modelo Profile
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return f'{self.title} by @{self.user.username}'
