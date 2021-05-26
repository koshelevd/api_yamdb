# RESTful API "YAMdb"

Django-based RESTful API builded with Django Rest Framework.
YamDB is project with DB of movies, books and songs reviews.

## User registration algorithm
1. User sends request with `email` parameter to `\auth\email\`.
2. **YamDB** sends a letter with `confirmation_code` back to the `email`.
3. User requests `\auth\email\` with `email` and `confirmation_code` 
   parameters, then gets `token` (JWT) in response.
4. Optionally the user sends a PATCH request to `/users/me/` and fills in 
   the fields in his profile (the description of the fields is in the documentation).  

## User roles
- **Anonymous** - can view descriptions of works, read reviews and comments.
- **Authenticated user** - can read everything like **Anonymous**, in 
  addition he can publish reviews and rate works (films/books/songs), 
  can comment on other people's reviews and rate them; 
  can edit and delete **own** reviews and comments.
- **Moderator** - the same rights as the **Authenticated user** plus the 
  rights to delete any reviews and comments.
- **Administrator** - full rights to manage the project and all its contents.
  Can create and delete categories and works. Can assign roles to users.
- **Django administrator** - the same rights as the **Administrator* role.   

## Authentication
- Security Scheme Type: **_API Key_**
- Header parameter name: **_Bearer_**

## Requests
API requests starts with `\api\v1`

## Installing on a local machine 

This project requires python3.8 and sqlite.

- Install requirements:
  ```
  $ python -m venv venv
  $ source ./venv/scripts/activate
  ```
  ```
  $ python manage.py migrate
  $ python manage.py collectstatic
  $ python manage.py createsuperuser
  ```
- Start development server:
  ```
  $ python manage.py runserver
  ```
## Documentation
