from django.forms import ModelForm
from .models import SurfboardRoom

# Create your forms here.


class RoomForm(ModelForm):
    class Meta:
        model = SurfboardRoom
        fields = '__all__' # creates form based on fields from the SurfboardRoom Model Class
        # fields = ["name", "body"] # creates form based on fields on this list