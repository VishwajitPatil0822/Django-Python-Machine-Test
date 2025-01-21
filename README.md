
# About DRF Based Client Project Management API

The DRF Based Client Project Management API is a comprehensive and scalable solution designed to simplify the management of clients and their projects within organizations. Built using the powerful Django REST Framework (DRF), this RESTful web service enables businesses to efficiently handle client registrations, project assignments, and user collaborations. It provides an intuitive API to allow authenticated users to perform CRUD operations on clients and projects while ensuring that multiple users can be assigned to a single project, facilitating team-based work. The API adheres to RESTful principles, ensuring a seamless integration experience with front-end applications, mobile platforms, or any third-party services.

With the use of Django for backend development and a reliable MySQL database for data storage, this API guarantees security, scalability, and robust performance. The system supports efficient management of multiple clients and their associated projects, empowering businesses to track progress, allocate resources, and collaborate across teams effortlessly. Whether you are building a custom client-project management solution or seeking to extend this API for your business needs, this project offers a solid foundation for seamless operations. Designed for businesses of all sizes, it is ideal for companies looking to optimize their project management workflow while ensuring ease of use, security, and scalability.



## Key Features
#### Client Management:

* Register new clients
* Retrieve client information
* Update or delete existing clients
* Project Management:

#### Add new projects under a client
* Assign multiple users to projects
* Retrieve project details

#### User Assignments:
* Assign users to multiple projects
* Fetch projects assigned to the logged-in user
## System Overview

* Users: The system supports multiple users with different roles.
* Clients: Each client can have multiple projects.
* rojects: Projects can be assigned to multiple users for collaboration.

  
## API Endpoints

| Endpoint          | Method     |  Description                                |
|-------------------|------------|---------------------------------------------|
| /client/	        | GET        | Fetch all clients                           |
| /client/	        | POST	     | Register a new client
| /client/<int:pk>/ |  GET       | Retrieve a specific client by ID
| /client/<int:pk>/	| PUT        | Update client details
| /client/<int:pk>/	| DELETE     |Remove a client
| /project/	        |   GET	     | Fetch all projects
| /project/	        | POST	     | Create a new project
| /project/<int:pk>/| GET        |Retrieve a specific project by ID
| /project/<int:pk>/| PUT        |Update project details
| /project/<int:pk>/| DELETE     | Delete a project


## Super Users Id / Password

| User Name         |  Password     |
|-------------------|---------------|
| admin	            |  admin        |
| user1	            |  demo@123     |
   

     
## Authentication
* The API is protected using session-based authentication (by default).
* For API access, login using Django's built-in admin panel at /admin/.
* DRF's browsable API authentication is available at /api-auth/.




## Technologies Used
* Framework: Django 5.1
* Database: MySQL
* Authentication: Django’s built-in authentication system
* Serialization: DRF serializers for data validation and processing
* Security: Token-based authentication (recommended for production)




## Installation & Setup

1. Clone the repository:
                  
            git clone https://github.com/VishwajitPatil0822/Django-Python-Machine-Test.git   

            cd your-repo


2. Create a virtual environment and activate it:

           python -m venv venv
   
           source venv/bin/activate


3. Install dependencies:
         
          pip install -r requirements.txt  



4. Configure database settings in 'settings.py'

 DATABASES = {
 
         'default': {
         
                 'ENGINE': 'django.db.backends.mysql',
                 
                 'NAME': 'client_project_management_system_db',
                   
                 'USER': 'root',
                  
                 'PASSWORD': 'root',
                 
                 'HOST': 'localhost',
        
                 'PORT': '3306',
        
              }
        }


5. Apply migrations and start the server:
    
                  python manage.py migrate  
                  python manage.py runserver  





