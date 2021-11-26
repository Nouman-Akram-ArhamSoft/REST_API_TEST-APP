# ToDoApp-Class-Base-API-Project
This is ToDo Class Base REST API Application with JWT on Django with connection of Postgresql

# Setup

## Install Requirements 
 command : 
 ``` 
 pip3 install -r requirements.txt 
 ```
for run the virtual envoirement 

``` 
virtualenv env 
```
``` 
.source env/bin/activate 
```

### Clonning Project:

``` 
git clone https://github.com/Nouman-Python-Developer/REST_API_TEST-APP.git 
```

## Run Server Detail:
 command : 
 ``` 
 python manage.py runserver 
 ``` 
 on ubuntu : 
 ``` 
 python3 manage.py runserver 
 ```
 
 
 after connecting database run these commands
 ``` 
 python3 manage.py makemigrations 
 ```
 ``` 
 Python3 manage.py migrate  
 ```
 
 ## for Main Page:
 http://127.0.0.1:8000/
 
 ## for Swagger Documentations:
 http://127.0.0.1:8000/swagger
 After successfully access we can register the user and login it at login API
 
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
 
 [Database Postgresql Connection with Django](https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8)
 
 # Results
 **Pylint result 9.41/10**
  ```
 pylint todo_api
 ```
 
 ![Pylint Result](https://user-images.githubusercontent.com/93263475/143041995-17444ae7-8430-4f8a-911e-1e04044e68c3.png)
 
 **Test Cases Result: All Test Passed**
 
 > if u see error:
 **django user has no permission createdatabase** Run below command on postgresql cmd.
 ```
 Alter User User(Django user name) CreateDB;
 ```
 
 For run the test:
 ```
 python3 manage.py test
 ```
 
![Unit Testing Result](https://user-images.githubusercontent.com/93263475/143042032-13bb90b9-4a73-47e3-9e9f-dbcfa2339c89.png)

 
 
