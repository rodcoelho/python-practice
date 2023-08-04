from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
Django has Models out of the bag. 
Here we are taking advantage of their User Model (see Room's host attribute).
"""

class Topic(models.Model):
    # shaper topics

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    # surfboard rooms

    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    link = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)

    class Meta:
        ordering = ['-updated', '-created'] # sorts the data by elements in this list

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    # surfboard messages

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created'] # sorts the data by elements in this list

    def __str__(self):
        return str(self.body[0:50])


