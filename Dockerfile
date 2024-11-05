# Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the app directory into the container
COPY app /app/app

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Ensure the data directory exists with proper permissions
RUN mkdir -p /app/app/data && chmod -R 777 /app/app/data

# Expose port 8000
EXPOSE 8000

# Run the FastAPI application with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
