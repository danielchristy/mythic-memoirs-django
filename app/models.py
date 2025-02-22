from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_email
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(validators=[validate_email], max_length=100, blank=False)

    def __str__(self):
        return self.first_name

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.TextField(null=True, blank=True, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    # def tag(self):
    #     if self.tags:
    #         return self.tags.split(',')
    #     return []

    def __str__(self):
        return self.name

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    tags = models.TextField(null=True, blank=True, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    # def tag(self):
    #     if self.tags:
    #         return self.tags.split(',')
    #     return []

    def __str__(self):
        return self.title

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    tags = models.TextField(null=True, blank=True, max_length=255)
    date_created = models.DateField(auto_now_add=True)

    # def tag(self):
    #     if self.tags:
    #         return self.tags.split(',')
    #     return []
    
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=255)
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    characters = models.ManyToManyField(Character)
    summary = models.TextField()
    location = models.ManyToManyField(Location)
    tags = models.TextField(null=True, blank=True, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    # def character(self):
    #     if self.characters:
    #         return self.characters.split(',')
    #     return []
    
    # def tag(self):
    #     if self.tags:
    #         return self.tags.split(',')
    #     return []

    def __str__(self):
        return self.id