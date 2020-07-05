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
python manage.py sqlmigrate blog 0001
```

and it will return something that looks like this:

```unix
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL, "date_posted" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;
```

You then want to run the migration to actually change the database.

```unix
python manage.py migrate
```

You should get an OK status if it is ok
