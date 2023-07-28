from django.contrib import admin

# Register your models here.

from .models import SurfboardRoom, ShaperTopic, Message

admin.site.register(SurfboardRoom)
admin.site.register(ShaperTopic)
admin.site.register(Message)