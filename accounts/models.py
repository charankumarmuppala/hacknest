from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_photo = models.FileField(upload_to='profiles/', null=True, blank=True)
    college = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    year_of_study = models.CharField(max_length=50, null=True, blank=True)
    about_me = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
