from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Room, Topic
from .forms import RoomForm

# Create your views here.


def home(request):
    # get the q from search in the navbar.html
    q = request.GET.get("q") if request.GET.get("q") != None else ''

    rooms = Room.objects.filter( # multiple queries using OR statement
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
        )
    room_count = rooms.count()

    topics = Topic.objects.all()

    context = {"rooms": rooms, "topics": topics, "room_count": room_count}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)

    context = {"room": room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()

    if request.method == "POST":
        form = RoomForm(request.POST) # pass the POST values to the form
        if form.is_valid():  # check if form is valid
            form.save()  # save to db
            return redirect("home") # redirect them after to home

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room) # instance allows us to inject the room instance data into the form

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room) # 

        if form.is_valid():
            form.save()
            return redirect("home")

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect("home")

    context = {'obj': room}
    return render(request, 'base/delete.html', context)
