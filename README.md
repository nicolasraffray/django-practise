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

### Querying the database using the ORM models

we can query the database using the django ORM. The django-python shell will let us work with these models interactively.

```unix
python manage.py shell
```

Then in python

```python
from blog.models import Post
from django.contrib.auth.models import User

# Get all users
User.objects.all()
# Get first user
User.objects.first()
# Filter
user = User.objects.filter(username = 'nic')

# Look at attributes
user.pk # primary key

# Getting users
user = User.objects.get(id = 1)

# --- # 

# Createing a new post
post_1 = Post(title='blog1', content='first post content', author=user) # alternatively you can run author_id = user.id

# This will have created a new post but it has not been saved to database.

post_1.save()

Post.objects.all() # You will see the post has now been saved.

# --- #

# Getting all posts by a specific user with query set
user.post_set.all()

# Posts can also be created in this fashion
user.post_set.create(title="new post", content="yet another post") # don't need author bc Django knows from user.post_set. You dont need to save either is saved automatially

```
