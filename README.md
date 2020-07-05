# Django Practise

## Admin and DataBase Setup

To create a new user run in terminal.

1. Create a database

```unix
python manage.py migrate
```

Will create an auth user table along with running other default migrations.

2. Create a superuser

```unix
python manage.py createsuperuser
```

3. Fill in the superuser credentials.

## Database in Django

Django has its own ORM! It will let us represent the database structure as classes, or models.

Each class is its own table in the database and the attributes are different fields in the database.

Once a new model is created the migrations need to be made

```unix
python manage.py makemigrations
```

If you want to see the sql of the migrations type something like the following

```unix
python manage.py sqlmigrate blog 00001
```
