from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


from .models import Room, Topic, Message
from .forms import RoomForm, TopicForm

# Create your views here.

def loginPage(request):

    page = 'login'

    # don't let logged in people login again
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            # django flash message
            messages.error(request, "User does not exist")
        
        # authenticate checks that the user exists and returns a user object
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # adds user session to db & to browser
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username OR Password does not exist")

    context = {"page": page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect("home")

def registerPage(request):
    
    form = UserCreationForm()
    context = {"form": form}

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # save user locally, don't commit to db yet
            # commit == false so that we can clean up the data before saving
            user = form.save(commit=False)  

            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occurered during registration")

    return render(request, 'base/login_register.html', context)

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
    room_messages = Message.objects.filter(
        Q(room__topic__name__icontains=q)
        )

    context = {
        "rooms": rooms, "topics": topics, 
        "room_count": room_count, "room_messages": room_messages
        }
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all() # get children of the parent model, message in this case (<parent>.<child>_set.all())
    participants = room.participants.all()

    if request.method == "POST":
        room_message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get("body")
        )

        # add user to participants now that he has commented
        if request.user not in participants:
            room.participants.add(request.user)
        return redirect("room", pk=room.id)

    context = {"room": room, "room_messages": room_messages, "participants": participants}
    return render(request, 'base/room.html', context)


@login_required(login_url="login")
def createRoom(request):
    form = RoomForm()

    if request.method == "POST":
        form = RoomForm(request.POST) # pass the POST values to the form
        if form.is_valid():  # check if form is valid
            form.save()  # save to db
            return redirect("home") # redirect them after to home

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url="login")
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room) # instance allows us to inject the room instance data into the form

    if request.user != room.host:
        return HttpResponse("You are not allowed to perform action")

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room) # 

        if form.is_valid():
            form.save()
            return redirect("home")

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url="login")
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("You are not allowed to perform action")

    if request.method == 'POST':
        room.delete()
        return redirect("home")

    context = {'obj_to_delete': room}
    return render(request, 'base/delete.html', context)


def createTopic(request):
    form = TopicForm()

    if request.method == "POST":
        form = TopicForm(request.POST) # pass the POST values to the form
        if form.is_valid():  # check if form is valid
            form.save()  # save to db
            return redirect("home") # redirect them after to home

    context = {'form': form}
    return render(request, 'base/topic_form.html', context)


@login_required(login_url="login")
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("You are not allowed to perform action")

    if request.method == 'POST':
        message.delete()
        return redirect("home")

    context = {'obj_to_delete': message}
    return render(request, 'base/delete.html', context)
