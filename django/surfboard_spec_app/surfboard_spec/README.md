# Cheatsheet

### Django Model
        A django Project has many Apps
                ----> APP 1
        Project ----> APP 2
                ----> APP 3

    -------------------------------------
        Workflow 
                                      ---> Models         
        Settings ---> URLs ---> Views ---> Templates
                                      ---> Forms

# Django Commands 

    python3 manage.py runserver
    python3 manage.py makemigrations
    python3 manage.py migrations


# Starting a new Project

    # start boilerplate for a new django project
    django-admin startproject <PROJECT_NAME>

    # this creates a new APP within the project, creates boilerplate directory APP
    python3 manage.py startapp <APP_NAME> 

    # then you need to add the new APP_NAME to the INSTALLED_APPS in settings.py ---> '<PROJECT_NAME>.<APP_NAME>.BaseConfig' so that Django picks up your local app

    # Now you're ready to begin adding to the APP. Follow the logic of adding thigns by following the Settings->Url->V->MT Workflow


--------

# Modifying the APP w/ URL->V->MT Workflow

    
    ### Settings ###

    Where Django finds Apps, Templates, Database, and other settings

    
    ### URLs ###
    
    # Django looks inside `<PROJECT_NAME>/urls.py` for project level urls.
    # By including `path("", include("<APP_NAME>.urls"))` in the urlpatterns, we tell Django to check `<APP_NAME>/urls.py` for other app specific urls.

    
    ### Views ###

    # URLs are mapped to views in urls.py. The view classes and functions live in <APP_NAME>/views.py. 
    # Within views, you CRUD the models in <APP_NAME>/models.py and inject/retrieve info from the files in <APP_NAME>/templates/<APP_NAME>/*.html (Django needs this path structure to combine all the templates in the project and in the app)


    # How to use Models within Views
    MODEL_NAME.objects.create(...)                                # create a new object
    MODEL_NAME.CHILD_NAME_set.all()                               # get children of the parent model <parent>.<child>_set.all()
    MODEL_NAME.objects.all()                                      # get all objects for that Model
    MODEL_NAME.objects.filter()                                   # filter objects by a column attribute (effectively no filter)
    MODEL_NAME.objects.filter(ATTRIBUTE="xzy")                    # filter objects by some parameter == "xyz"
    MODEL_NAME.objects.filter(ATTRIBUTE__CHILDATTRIBUTE="xzy")    # filter objects by accessing the child Model's parameter using the dunder "__"
    MODEL_NAME.objects.filter(ATTRIBUTE__icontains="xzy")         # filter objects by some parameter containing xyz (not case sensitive)
    model_object = MODEL_NAME.objects.filter(                     # filter object by using an OR statement
        Q(ATTRIBUTE_1__icontains = q) |
        Q(ATTRIBUTE_2__icontains = q)
    )
    model_object = MODEL_NAME.objects.filter(                     # filter object by using an AND statement
        Q(ATTRIBUTE_1__icontains = q) &
        Q(ATTRIBUTE_2__icontains = q)
    )

    # Request objects
    request.GET.get("username")
    request.POST.get("username")
    request.user.is_authenticated

    # Auth within Views
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # adds user session to db & to browser
        login(request, user)
        return redirect('home')


    ### Models ###

    # Models are ORMs that we can leverage to CRUD data. 
    # Model attributes/columns can be of type Field or ForeignKey (another key in another table)
    #   max_length=200              # set the max
    #   on_delete=models.SET_NULL   # if the parent object is deleted, set this value to null
    #   on_delete=models.CASCADE    # if the parent object is deleted, also delete this object
    #   auto_now=True               # good for updating time each time
    #   auto_now_add=True           # only updates once when object created
    #   null=True                   # can be null
    #   blank=True                  # can be blank

    # Model fields
    models.ForeignKey(OTHER_MODEL_CLASS)
    models.CharField()
    models.TextField()
    models.DateTimeField()
    models.ManyToManyField(OTHER_MODEL_CLASS, related_name='NAME_OF_THIS_FIELD') # we only need related_name param if OTHER_MODEL_CLASS is already being referenced in another field as a foreign key

    # Everytime you make a new model, you'll need to migrate the db to take in the new model
        python3 manage.py makemigrations
    # And then apply migrations to the database, see changes in <APP_NAME>/migrations/
        python3 manage.py migrate    


    ### Templates ###

    # Templates are Django's use of Jinja injection to create dynamic pages. 
    # Parent templates live in /templates/*.html that can be inherited by <APP_NAME>/templates/<APP_NAME>/*.html (Django needs this path structure to combine all the templates in the project and in the app)


    ### Forms ###

    # Model objects that Django uses for forms. Create forms in <APP_NAME>/forms.py and access them in views to quickly create forms that map to models and can be passed to the template. On submit, we can save these forms to the original model. 


    ### Admin ###

    http://127.0.0.1:8000/admin
    # To create admin user
    python3 manage.py createsuperuser


# Jinja CheatSheet

    {% include 'COMPONENT.html' %}

    {% extends 'PARENT_TO_INHERIT_FROM.html' %}

    {% block content %}
    {% endblock content %}

    {% for item in items %}
    {% endfor %}

    {% url 'name-of-url' %}
    
    <form method="POST" action="">
        {% csrf_token %}
        {{form.as_p}}           # injects form with paragraph styling
        <input type="submit" value="Submit">
    </form>

    {% url 'home' %}?q={{topic.name}}    # this is a query -> ?q=

    {% if request.user.is_authenticated %}
    {% endif %}


# static files

    {% load static %}                           # to access the static folder
    "{% static 'images/surfboards.jpeg' %}"     # to access the static file



TIME: 4:54:33
