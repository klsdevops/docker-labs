# flask-docker-lab
This is a lab for docker image build and test. 
For our lab, you're going to containerize a simple Python web application by writing a Dockerfile from scratch. I've created a GitHub repository with the starter code and step-by-step instructions in this README.md file. Please navigate to the repo now, and let's get building!

### Directory Structure

This is the recommended structure for your lab's GitHub repository. The student will start their work inside the `app/` directory.

```
flask-docker-lab/
├── app/
│   ├── main.py
│   └── requirements.txt
│
└── solution/
    ├── Dockerfile
    └── .dockerignore
```

-----

### Starting Files (The `app/` Directory)

Copy or Create these files at the beginning of the lab.

#### **`app/main.py`**

This is a minimal web server that listens on port 5000 and returns a simple message.

```python
from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def hello_world():
    """A simple endpoint that returns a greeting."""
    return '<h1>Hello from inside a Docker Container!</h1>'

if __name__ == '__main__':
    # Run the app, listening on all network interfaces on port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
```

#### **`app/requirements.txt`**

This file lists the Python dependencies needed for the application.

```
Flask==2.2.2
```
#### NOTE:
If you want to demonstrate a real-time problem and solution, do not update the requirements.txt file with all the dependencies, then it will throw errors. Later as a solution, add the below to the requirements.txt and rebuild the image.
```
Flask==2.2.2
Werkzeug==2.2.2
```

-----

### Solution Files (The `solution/` Directory)

Students are expected to create these files by themselves by the end of the lab. Hence I'm keeping them in a separate `solution/` folder for them to reference.

#### **`solution/Dockerfile`**

This is the optimized, complete `Dockerfile` that correctly containerizes the application.

```dockerfile
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
```

#### **`solution/.dockerignore`**

This file prevents unnecessary or sensitive files from being copied into the build context, keeping the final image small and secure.

```
# Git files
.git
.gitignore

# Python cache and virtual environment files
__pycache__/
*.pyc
*.pyo
*.pyd
.venv/
venv/
env/

# IDE and OS-specific files
.idea/
.vscode/
*.DS_Store
```
