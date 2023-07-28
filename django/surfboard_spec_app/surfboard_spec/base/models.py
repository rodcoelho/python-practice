from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
Django has Models out of the bag. 
Here we are taking advantage of their User Model (see SurfboardRoom's host attribute).
"""

class ShaperTopic(models.Model):
    # columns

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SurfboardRoom(models.Model):
    # columns

    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    shaper_topic = models.ForeignKey(ShaperTopic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # participants = models...

    class Meta:
        ordering = ['-updated', '-created'] # sorts the data by elements in this list

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    # columns

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    surfboard_room = models.ForeignKey(SurfboardRoom, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.body[0:50])


