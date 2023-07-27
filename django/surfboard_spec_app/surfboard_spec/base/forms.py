from django.forms import ModelForm
from .models import Room

# Create your forms here.


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # creates form based on fields from the Room Model Class
        # fields = ["name", "body"] # creates form based on fields on this list