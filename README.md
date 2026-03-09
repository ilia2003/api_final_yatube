# Yatube API

RESTful API for the **Yatube social network**.  
The API allows users to interact with the platform programmatically: create posts, comment on publications, subscribe to authors, and retrieve community information.

The project demonstrates backend development with **Django REST Framework**, authentication using **JWT**, and implementation of social platform features.

---

# Features

The API provides the following functionality:

### Posts
- Create posts
- Edit posts
- Delete posts
- Retrieve a list of posts

### Comments
- Add comments to posts
- Edit comments
- Delete comments
- View comments for a specific post

### Communities
- Retrieve a list of communities
- View community details

### Subscriptions
- Follow authors
- View user subscriptions

### Authentication
- Obtain JWT tokens
- Refresh access tokens
- Verify tokens

---

# Tech Stack

Backend:

- Python
- Django
- Django REST Framework

Authentication:

- JWT (JSON Web Token)

Tools:

- Git
- SQLite / PostgreSQL

---

# Architecture


Client
↓
Django REST API
↓
Business Logic
↓
Django ORM
↓
Database


Main entities:

- Users
- Posts
- Comments
- Groups (communities)
- Subscriptions

---

# Installation

### 1 Clone repository

```bash
git clone https://github.com/polina-dianova/api_final_yatube.git
cd api_final_yatube
2 Create virtual environment

Linux / MacOS

python3 -m venv env
source env/bin/activate

Windows

python -m venv env
env\Scripts\activate
3 Upgrade pip
python -m pip install --upgrade pip
4 Install dependencies
pip install -r requirements.txt
5 Apply migrations
python manage.py migrate
6 Run development server
python manage.py runserver
API Documentation

After starting the server, interactive API documentation will be available at:

http://localhost:8000/redoc/
API Examples
Create a Post

Request:

POST /api/v1/posts/

Body:

{
  "text": "Hello, this is my first post!",
  "group": 1
}

Response:

{
  "id": 12,
  "author": "admin",
  "text": "Hello, this is my first post!",
  "pub_date": "2025-01-10T15:30:00Z",
  "image": null,
  "group": 1
}
Get Community Information

Request:

GET /api/v1/groups/2/

Response:

{
  "id": 1,
  "title": "Sport",
  "slug": "sport",
  "description": "Group for discussing sports events."
}
Follow an Author

Request:

POST /api/v1/follow/

Body:

{
  "following": "john_doe"
}

Response:

{
  "id": 4,
  "user": "admin",
  "following": "john_doe"
}
Development Purpose

This project demonstrates:

REST API design

Authentication with JWT

Social network backend logic

Django REST Framework usage

API documentation with ReDoc

Author

Ilya Fedorenko
