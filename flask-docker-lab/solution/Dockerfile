# Start from a lightweight, official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency file first to leverage Docker's build cache
COPY app/requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application source code
COPY app/ .

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "main.py"]