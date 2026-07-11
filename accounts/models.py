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


import random
import string

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=6, unique=True, blank=True)
    hackathon = models.CharField(max_length=150)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_teams')
    members = models.ManyToManyField(User, related_name='joined_teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        while True:
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            if not Team.objects.filter(code=code).exists():
                return code

    def __str__(self):
        return self.name
