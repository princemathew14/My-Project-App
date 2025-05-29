## Project Management System (Django + PostgreSQL)

This is a Django-based web application for managing software projects, tasks, users, comments, and time logs.
It allows project teams to track task progress, log hours, and collaborate via comments.

Domain
Application Domain: Project Management
This system models real-world workflows between developers, designers, project managers, and QA engineers using:

Projects
Users
Tasks (assigned to users per project)
Comments (attached to tasks)
Time Logs (to track effort)
Setup Instructions
1. Clone the Repository
git clone https://github.com/princemathew14/My-Project-App.git

cd Django-Assignment-01 2. Create a Virtual Environment python -m venv venv

Activate the environment:
source venv/bin/activate # On Unix/macOS venv\Scripts\activate # On Windows 3. Install Dependencies

pip install -r requirements.txt Environment Configuration

Create a .env File (in the project root) Copy the template and fill in your actual credentials: cp env.example .env
Edit .env and fill in: SECRET_KEY='your-django-secret-key' DEBUG=True DATABASE_URL='postgres://your_db_user:your_db_password@localhost:5432/your_db_name' Make sure your PostgreSQL database is created and running.
Migrations & Superuser

Apply Migrations python manage.py makemigrations python manage.py migrate

Create a Superuser python manage.py createsuperuser

Enter username, email, and password as prompted

Run the Development Server python manage.py runserver Visit: http://127.0.0.1:8000/admin/ to access the Django Admin Dashboard.

Log in with your superuser credentials to manage Projects, Users, Tasks, Comments, and Time Logs. Admin Sample Data Use the admin interface to add 3–5 records for each model.

Make sure relationships (like tasks to users, comments to tasks) are linked.

Project Structure Overview

myproject/

myapp/ # App containing models, views, admin setup

myproject/ # Settings and main config

manage.py # Django entry point

.env # Environment variables (ignored by Git)

env.example # Sample env file to share

requirements.txt # All Python dependencies

##  CRUD Implementation Overview

CRUD Functionality Implemented

This Django project implements full CRUD operations (Create, Read, Update, Delete) for the Project model using Django's Class-Based Generic Views.

 Base URL Path

All views related to the Project model are accessible under:
/projects/

Example: http://localhost:8000/projects/

 Navigating CRUD Operations

Operation	URL Pattern	Description

List	/projects/	View all projects

Detail	/projects/<int:pk>/	View details of a specific project

Create	/projects/create/	Add a new project

Update	/projects/<int:pk>/update/	Edit an existing project

Delete	/projects/<int:pk>/delete/	Delete a project (with confirmation)

 How to Use
 
Visit http://localhost:8000/projects/

Click a project’s title to view details.

Click "Create New Project" at the bottom of the list to add a new project.

From a project’s detail page:

Click Edit to update it.

Click Delete to confirm and remove it.

After each action, a success message will be displayed.

##  Authentication & Authorization Setup Guide

Google OAuth Setup (django-allauth)

1. Create OAuth Credentials in Google Cloud Console

Visit: https://console.cloud.google.com/

Create a new project or choose an existing one

Go to APIs & Services → Credentials

Click “Create Credentials” → “OAuth Client ID”

If prompted, configure OAuth consent screen (choose "External")

Application type: Web application

Set Authorized Redirect URI to:

http://127.0.0.1:8000/accounts/google/login/callback/
Copy the generated:

Client ID

Client Secret

2. Add Credentials to .env
Edit your project’s .env file:

GOOGLE_CLIENT_ID=your-google-client-id-here

GOOGLE_CLIENT_SECRET=your-google-client-secret-here

Also make sure .env.example includes:

GOOGLE_CLIENT_ID=

GOOGLE_CLIENT_SECRET=

3. Configure Google Provider in settings.py

How to Test Login (Local and Google)

1. Local Login
Visit: http://127.0.0.1:8000/accounts/signup/ to register

Log in at: http://127.0.0.1:8000/accounts/login/

Log out at: http://127.0.0.1:8000/accounts/logout/

2. Google Login
Visit the login page

Click "Login with Google"

Authenticate using your Google account

On success, a Django user account is created (if not already present)

We are redirected to the homepage

 How to Test Permission Restrictions
These assume we are using LoginRequiredMixin and UserPassesTestMixin in your Update/Delete views for models like Project.

 Logged-out User
Try accessing:

/projects/create/

/projects/1/update/

/projects/1/delete/

It will be redirected to the login page (/accounts/login/)

 Logged-in User
Can access the list and create pages

Can only edit/delete their own items (ownership enforced)

Will get a 403 Forbidden or redirect when trying to update/delete someone else’s project

 Superuser or Staff
Can update or delete any object, regardless of ownership

##  Django REST Framework (DRF) API Integration

This project now includes a fully functional RESTful API built with **Django REST Framework (DRF)**. It exposes key models through standard CRUD endpoints for use by frontend apps, mobile clients, or third-party services.



###  Base API URL

/api/


### Exposed Models via API

Currently, the following models are exposed:

- `Project`: `/api/projects/`

###  How to Test the API (Browsable API)

1. **Start the server**
   
   python manage.py runserver
Login via the browser
Visit:

http://127.0.0.1:8000/accounts/login/
Log in with your Django user credentials (use createsuperuser if needed).

Access the API
Navigate to:

http://127.0.0.1:8000/api/
we’ll see a browsable interface for our API endpoints.

Use HTTP methods

GET: View list or detail

POST: Create objects (authenticated only)

PUT / PATCH: Update

DELETE: Remove

Note: Most actions require to be logged in (IsAuthenticated permission).

 Optional: API Documentation
We enabled drf-spectacular, we can also access generated API docs:

Swagger UI:

http://127.0.0.1:8000/api/schema/swagger-ui/
Redoc UI:

http://127.0.0.1:8000/api/schema/redoc/
OpenAPI Schema (raw JSON):

http://127.0.0.1:8000/api/schema/
Example Git Commit

git add .
git commit -m "feat: Add DRF API endpoints"
git push
File Overview
myapp/serializers.py: Serializers for converting model instances to JSON

myapp/views.py: DRF ModelViewSet classes

myproject/urls.py: DRF router and API schema URLs

##  Django REST Framework – Advanced API Features

This Django REST API now supports **filtering**, **searching**, **ordering**, **pagination**, and **custom permissions** for more powerful and secure data access.


### Query Parameter Examples

We can append the following query parameters to our API list URLs (e.g., `/api/projects/`):

####  Filtering (`?field=value`)
Use model field names to return matching records:

/api/projects/?name=Website Redesign

/api/projects/?owner__id=2

 Searching (?search=term)

Search across multiple fields defined in the search_fields of the ViewSet:

/api/projects/?search=website

Ordering (?ordering=field)

Order results by a field in ascending or descending order:

/api/projects/?ordering=start_date

/api/projects/?ordering=-end_date

Pagination

Pagination splits results into pages to improve performance and usability.

Default Page Size: 5 items per page (configurable via PAGE_SIZE)

Use ?page= to navigate:


/api/projects/?page=1

/api/projects/?page=2

Response format includes:

{
  "count": 7,
  "next": "http://localhost:8000/api/projects/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Example Project",
      ...
    },
    ...
  ]
}
 Custom Permission: IsOwnerOrReadOnly

Read Access (GET, HEAD, OPTIONS): Allowed to any authenticated user.

Write Access (PUT, PATCH, DELETE): Only the owner of the object can modify it.

Enforced using a custom permission class IsOwnerOrReadOnly.

Example:

User A creates a project.

User B cannot edit or delete that project (403 Forbidden).

 How to Test Features

Prerequisites

Server running:

python manage.py runserver

Log in:

http://127.0.0.1:8000/accounts/login/

 Test Filtering/Searching/Ordering

Go to:

http://127.0.0.1:8000/api/projects/

Try:

?search=keyword

?ordering=start_date

?owner__id=1

 Test Pagination

Add enough projects (or reduce PAGE_SIZE).

Try:

/api/projects/?page=1

/api/projects/?page=2

 Test Permissions
 
Log in as User A and create a project.

Log out. Log in as User B.

Try to PATCH or DELETE User A's project.

we should receive: 403 Forbidden.

## Django + DRF Project (Dockerized)

This project is a containerized Django REST Framework application using PostgreSQL and django-environ for environment-based settings.

 Getting Started (Docker Compose)

1️ Build Docker Images

docker compose build

2️ Start Application

docker compose up -d

This starts:

web: Django app using Gunicorn

db: PostgreSQL container

3️ Stop Application

docker compose down

To stop and delete database volume (permanent data loss):


docker compose down -v

Setting Up .env

Copy the provided .env.example:

cp .env.example .env

Edit .env with your secret key and database credentials. Example:


SECRET_KEY='your-django-secret-key'

DEBUG=True

DATABASE_URL='postgres://your_user:your_password@db:5432/your_db'

POSTGRES_DB=your_db

POSTGRES_USER=your_user

POSTGRES_PASSWORD=your_password

Running Migrations

If migrations are not included in the startup command, run:


docker compose exec web python manage.py migrate

 Accessing the App

Main site: http://localhost:8000

DRF API root: http://localhost:8000/api/

Admin panel: http://localhost:8000/admin/




























































