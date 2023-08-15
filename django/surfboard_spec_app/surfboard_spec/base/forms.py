from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Room, Topic

# Create your forms here.


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # creates form based on fields from the Room Model Class
        # fields = ["name", "body"] # creates form based on fields on this list
        exclude = ['host', 'participants'] # excludes from the form


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__' # creates form based on fields from the Topic Model Class
        # fields = ["name", "body"] # creates form based on fields on this list