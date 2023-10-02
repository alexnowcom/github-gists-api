# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set environment variables for Flask
ENV FLASK_APP=github_gists_api.py
ENV FLASK_RUN_HOST=0.0.0.0

# Create and set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 8080 for Flask to listen on
EXPOSE 8080

# Define the command to run your application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
