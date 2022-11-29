A simple django web app demo

### Create a new django web project
    django-admin startproject django_web_app

### Run development server
    python manage.py runserver

### Create a new django "app"
    python manage.py startapp my_app

### Creating a user
    python manage.py createsuperuser

### Migration Workflow
```
# Make sure your app is in INSTALLED_APPS
# Step 1: Change model code
# Step 2: Generate migration script
python manage.py makemigrations

# Show migrations
python manage.py showmigrations

# Apply migrations
python manage.py migrate
```
