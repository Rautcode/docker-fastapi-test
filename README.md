# Dockerized FastAPI Application

This is a FastAPI application that allows users to create and read user data stored in a JSON file. The application is containerized using Docker for easy deployment.

## Features

- Create user data with first name, last name, and age.
- Read all user data from a JSON file.
- Data is stored in a `users.json` file within a `data` directory.

## Prerequisites

- Docker installed on your machine
- Docker Compose (if using docker-compose)

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/Rautcode/docker-fastapi-test.git
cd docker-fastapi-test

### Interactive API Documentation

FastAPI automatically generates interactive API documentation that you can use to test the endpoints. 

1. **Access the Documentation**:
   - Open your web browser and navigate to: [http://localhost:8000/docs](http://localhost:8000/docs)

2. **Testing the API**:
   - To **Get Users**:
     - Click on the `GET /users` endpoint in the documentation.
     - Click the **"Try it out"** button.
     - Then click **"Execute"** to see the output.
   - The actual output will be shown below the request section, displaying the user data from the `users.json` file.

### Example Output

After executing the **Get Users** request, you might see a response like this if there are no users yet:

```json
{
  "data": []
}
