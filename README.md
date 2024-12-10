# Django Framework Setup


# Old way of creating Virtual environment
-> python -m venv .venv


# uv is exptereamly fast package manager written in rust
# Install the uv using pip
-> pip install uv


# Creates a new virtual environment using uv at .venv
-> uv venv

# Setting Execution Policy
# Set Execution Policy for Current User: Applies the RemoteSigned policy to your user account only.
-> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# This will initilize the virtual environment
-> .venv/Scripts/activate


# Install Django using uv
-> uv pip install Django

# Start Django Projeect
-> django-admin startproject chaiaurDjango

# Go to Project folder
-> cd chaiaurDjango

# Run the app using manage.py and runserver
-> python manage.py runserver

# Now the server will be running at port 8000
-> Check out the app - http://127.0.0.1:8000/

# If you want to run on specific port. Ex- port - 8001
-> python manage.py runserver 8001


# File Exploration

## manage.py
This file is the starting point for the app. This file sets the environment varialbles and many other
-> What it does: The main command-line tool for interacting with your project.
-> What you can do:

    -> Run your development server:         python manage.py runserver
    -> Apply database migrations:           python manage.py migrate
    -> Create a new app:                    python manage.py startapp appname

You’ll use this file a lot during development.


## settings.py
What it does: The most important file for your project settings.
What it contains:
    -> Database configurations (SQLite is the default).
    -> Installed apps (like Django admin, authentication, etc.).
    -> Middleware (handles requests and responses).

When to use: Modify this file to set up your database, installed apps, and project-specific settings.


## urls.py

What it does: Manages the URL routing for your application.
What it contains:
    -> Links URLs to specific views or functionality.
    -> When to use: Add new paths here to handle different parts of your website.


## db.sqlite3
What it is: The default database for your project (SQLite).
Why it's used: It stores your application's data (like user accounts, blog posts, etc.).
When to use: SQLite is great for small projects or learning. For larger projects, you might switch to PostgreSQL or MySQL.

## Summary of Key Files:
-> settings.py: Configure your project (apps, database, etc.).
-> urls.py: Map URLs to views (webpages).
-> manage.py: Command-line tool for running the server and managing the project.
-> db.sqlite3: Your database.
As a beginner, focus on settings.py, urls.py, and manage.py as they are the most crucial for understanding Django projects.




# Creating basic views and urls
-----------------------------------------------------------------
|    User -> req -> urls -> views    (<- responses back)        |
-----------------------------------------------------------------

## Create view.py in the folder where urls.py is

-> Write the logic code.
-> views are similar to controllers in JavaScript where all the logic is written
-> create three functions/methods. home, about, contact. Return some text

## urls.py 
-> This works as router
-> Now write the code for different paths
-> Name the paths - home, about, contact and route them to the functions/methods in views file

    Ex- path('about/', views.about, name='about')

        -> views.about  - is the routing
        -> 'about/'     - is the url when this is hit it will return the logic of that funciton/method 


# Templates and Static in Django
![alt text](image.png)
-> On the root folder create a folder called 'templates'        -   Stores HTML files

-> Create another fodler called 'static'                        -   Stores CSS, JavaScript files


## Templates
-> Inside create a file 'index.html'

## How to show index.html on root url ?
-> To do this we have to render the tempalte
-> go to views.py - modify the code
    
      from django.shortcuts import render
      return render(request, 'index.html')


## Set the views to render on views in setting
-> The home page above will not render because in the settings the templates folder is not defined in directories
-> go to settings.py 
-> check for 'TEMPLATES' array

            in              ->  'DIRS': [],
            change it to    ->  'DIRS': ['templates'],

-> Now if you want to make new folder website and place the index.html in that folder then you can do it.
-> But you have to modify it in the views -> return render(request, 'website/index.html')


## How to show CSS and JavaScript in Django
-> In Static create a file 'style.css'
-> Now to link css to index.html we need to do 'templating engine' 

-> In index.html

            {% load static %}
            <link rel="stylesheet" href="{% static 'style.css' %}">

-> In settings.py
-> go to static url

        import os
        go to       - STATIC_URL

        Add this below code:

        STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static)]

-> Now you can see the css working


# Creating apps in Django
-> python manage.py startapp <App Name> 
    Ex- python manage.py startapp chai

After this 

Step-1
-------
-> The project is not aware of this newly created app
-> We need to make the main project aware of this new app

-> go to settings.py file
-> search for 'INSTALLED_APPS'

    add this -> 'chai',


step-2
-------
-> Now evey app is a stand alone app. So we can create the templates in this apps as well and then export them when needed to have modlularity
-> in folder 'chai' -> create a new folder 'tempaltes'

-> Industry standard
-> you create a sub folder in templates with the same name as app name (i.e. chai)
-> And in that you create the html 

-> There is bug here. Because of django configuration we will not have access to emmet in this folder. so we need to explicitly tell that there are html files in this folder
-> To do that. follow step below
-> Press ctrl + , 
-> you will go to settings
-> search for 'emmet: include language'
-> Add Item -> django-html and in value - html

-> This will make sure we get the emmet suggestions for html but still this will be a django template


step-3
-------
-> Now the same thing go to views and define the methods/functions
-> After that we need to route this into url but we don't have any url in this app folders

-> We have to create urls in our each app
-> best practice is to copy the project urls which is the main one and paste the same in this app

-> But there is one main thing to do here is to pass the control to this sub-urls from the main urls
-> Go to the main project urls.py (which is chaiaurDjango/urls.py)

        from django.urls import path, include

        urlpatterns = [
                            path('chai/', include('chai.urls')),
                      ]


-> Now go to the chai/urls.py

        urlpatterns = [
                            path('', views.all_chai, name='home'),
                      ]

-> Now run the project and hit the http://127.0.0.1:8000/chai url and see the output

-> Now like this you can create as many apps as you want


