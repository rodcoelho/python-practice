from rest_framework import serializers
from .models import Room


# Serializers take Django Models and makes it into JSON for the front end
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')