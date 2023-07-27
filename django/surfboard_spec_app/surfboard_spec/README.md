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

    {% extends 'PARENT_TO_INHERIT.html' %}

    {% block content %}
    {% endblock content %}

    {% for item in items %}
    {% endfor %}

    {% url 'name-of-url' %}
    
    <form method="POST" action="">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Submit">
    </form>


TIME: 2:06:23