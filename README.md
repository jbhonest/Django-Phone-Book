# Django Phone Book

This is a Django web application for managing contacts. The project includes a web interface and REST API endpoints for CRUD operations on contacts.

## Features

- Add, view, update, and delete contacts through a web interface.
- Search for contacts based on first name, last name, phone number, or address.
- REST API endpoints for interacting with contacts programmatically.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/jbhonest/django-phone-book.git
```
2. In **phonebook_project** folder rename sample_settings.py to local_settings.py
3. Generate a SECRET_KEY and save it in local_settings.py

4. Navigate to the project directory:

```bash
cd django-phone-book
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

6. Apply migrations to set up the database:
```bash
python manage.py migrate
```

7. Run the development server:
```bash
python manage.py runserver
```

## Web Interface
* Open your browser and go to http://127.0.0.1:8000/ to access the web interface.
* Use the provided menu options to add, view, update, delete, and search contacts.

## API Endpoints
* Contact List: http://127.0.0.1:8000/api/contacts/
* Contact Detail: http://127.0.0.1:8000/api/contacts/{contact_id}/

Use tools like curl, httpie, or Postman to interact with the API.



## Django Admin
First create an admin user:
```bash
python manage.py createsuperuser
```
Then access the Django admin interface at http://127.0.0.1:8000/admin/ to manage contacts.


---
Developed by Jamal Badiee (jbhonest@yahoo.com)