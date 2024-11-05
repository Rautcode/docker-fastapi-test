Dockerized FastAPI Application (DevOps Machine Test)
This project features a FastAPI application designed for managing user data, allowing for the creation and retrieval of user profiles stored in a JSON file. The application is packaged in a Docker container to facilitate straightforward deployment.

Key Features
Add new user profiles with fields for first name, last name, and age.
Retrieve all stored user profiles from a JSON file.
User data is saved in a file named users.json located within a data directory.
Interactive API Documentation
FastAPI provides automatic interactive API documentation, making it easy to test and explore the available endpoints.

Accessing the Documentation
Open your preferred web browser.
Navigate to http://localhost:8000/docs.
Using the API
To retrieve the list of users:

Locate the GET /users endpoint in the documentation.
Click the "Try it out" button.
Press "Execute" to see the results.
The response, showing the user information pulled from the users.json file, will be displayed below the request details.

Prerequisites
Before running the application, ensure you have the following installed:

Docker
Docker Compose 


Getting Started
Clone the Repository
To get started, clone this repository to your local machine:
git clone https://github.com/Rautcode/docker-fastapi-test.git
cd docker-fastapi-test
