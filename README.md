# ToDoApp-Class-Base-API-Project
This is ToDo Class Base REST API Application with JWT on Django with connection of Postgresql

# Setup
for run the virtual envoirement 

1. virtualenv env
2. .source env/bin/activate

### For new project:
3. pip install django (on ubuntu : pip3 install django)
4. django-admin startproject ToDoProject
5. ptyhon manage.py startapp ToDoApp

## Run Server Detail:
 command : python manage.py runserver (on ubuntu : python3 manage.py runserver) 
 
## Install Requirements 
 command : pip3 install -r requirements.txt 
 
 after connecting database run these commands
 **python3 manage.py makemigrations **
 **Python3 manage.py migrate **
 
 ## for Main Page:
 http://127.0.0.1:8000/
 
 ## for Swagger Documentations:
 http://127.0.0.1:8000/swagger
 After successfully access we can register the user and login it at login api
 
 # Features of Application
 
 ## Registration & Login API's
 
 1. Registration API for User
 2. Login API of User
 3. Password Rest API of User
 4. Confirm Password Rest API of User
 5. Show Self User Profile API
 
  ## JWT API's 
  
 1. Login API (for access the Refresh & access Token)
 2. Refresh Token API
 3. Verification Token API
 
  ## CRUD API's 
  
 1. Get Tasks API
 2. Get Specific Task API
 3. POST Task API
 4. PUT Task API
 5. Pathc Task API
 6. Delete Task API
 7. Soft Delete Task API
 
 
 # for Database Connection to Django:
 
 https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8
 
 # Results
 
 
 
 
