### Django SU->MVT Model

A django Project has many Apps

PROJECT = Settings + URL --> APP

                             APP == Views --> Models + Templates

### Django Commands

# runserver
python3 manage.py runserver

# db
django-admin makemigrations
django-admin migrations

# server
django-admin runserver


## Starting a new Project
Follow the logic of adding thigns by following the Settings->Url->V->MT Model

django-admin startproject <NAME>  # This starts boilerplate for a new django project
python3 manage.py startapp <APP> # this creates a new APP, creates boilerplate directory APP
# then you need to add the new APP to the INSTALLED_APPS in settings.py ---> '<NAME>.<APP>.BaseConfig',
# Then start by adding URLS 


## Settings

## URLS

## Views

## Models
python3 manage.py makemigrations     # once you make a new model, you'll need to migrate the db to take in the new model
python3 manage.py migrate            # applies migrations to the database found in the APP's migration directory

## Templates


## Admin

http://127.0.0.1:8000/admin
python3 manage.py createsuperuser # To create admin user