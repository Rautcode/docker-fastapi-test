Dockerized FastAPI Application (Devops Machine test)

This project features a FastAPI application designed for managing user data, allowing the creation and retrieval of user profiles stored in a JSON file. It is packaged in a Docker container to facilitate straightforward deployment.

Key Features
Add new user profiles with first name, last name, and age.
Retrieve all stored user profiles from a JSON file.
User data is saved in a file named users.json located within a data directory.
Interactive API Documentation
The FastAPI framework provides automatic interactive API documentation, allowing you to easily test the available endpoints.

Accessing the Documentation
Open your preferred web browser.
Go to: http://localhost:8000/docs
Using the API
To retrieve the list of users:

Find the GET /users endpoint in the documentation.
Click the "Try it out" button.
Press the "Execute" button to see the results.
The response will be displayed below the request details, showing the user information pulled from the users.json file.

Prerequisites
Before running the application, ensure you have the following installed:

Docker on your machine
Docker Compose 

Getting Started
Clone the Repository
To get started, clone this repository to your local machine:

bash
Copy code
git clone https://github.com/Rautcode/docker-fastapi-test.git
cd docker-fastapi-test
