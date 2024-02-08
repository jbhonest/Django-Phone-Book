# Django Phone Book

This is a Django web application for managing contacts. The project includes a web interface and REST API endpoints for CRUD operations on contacts.

## Features

- Add, view, update, and delete contacts through a web interface.
- Search for contacts based on first name, last name, phone number, or address.
- REST API endpoints for interacting with contacts programmatically.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jbhonest/django-blog-api.git
```
2. In **myblogproject** folder rename sample_settings.py to local_settings.py
3. Generate a SECRET_KEY and save it in local_settings.py


3. Navigate to the project directory:

```bash
cd django-blog-api
```

4. Install the required packages:

```bash
pip install -r requirements.txt
```

5. Apply migrations to set up the database:
```bash
python manage.py migrate
```


6. Run the development server:
```bash
python manage.py runserver
```
The API will be available at http://127.0.0.1:8000/api/.

## API Endpoints
* **Categories:** /api/categories/

    * List all categories and create a new category.
    * Individual category: **/api/categories/{category_id}/**

* **Posts:** /api/posts/

    * List all posts and create a new post.

    * Individual post: **/api/posts/{post_id}/**
* **Comments:** /api/comments/

    * List all comments and create a new comment.

    * Individual comment: **/api/comments/{comment_id}/**

## Django Admin
First create an admin user:
```bash
python manage.py createsuperuser
```
Then access the Django admin interface at http://127.0.0.1:8000/admin/ to manage categories, posts, and comments.


---
Developed by Jamal Badiee (jbhonest@yahoo.com)