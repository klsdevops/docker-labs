# LAB 1: flask-docker-lab
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

# LAB 2: nodejs-docker-lab

Copy or Create these three files in your "nodejs-docker-lab" project folder.

### package.json
(This file defines your app and its dependencies.)

```
JSON
```

```
{
  "name": "my-docker-app",
  "version": "1.0.0",
  "description": "Simple Docker app",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
```
### server.js
(This is your web server file.)

```
JavaScript
```
```
const express = require('express');

// Constants
const PORT = 3000;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  res.send('Hello from my Dockerized App!');
});

app.listen(PORT, HOST, () => {
  console.log(`Running on http://${HOST}:${PORT}`);
});
```

### .dockerignore
(This file tells Docker what to ignore.)

```
# Ignore dependencies on the host
node_modules

# Ignore git files
.git
.gitignore

# Ignore system files
.DS_Store

```

### Steps
1. **Setup:** download a simple app structure (e.g., a server file, a package.json, a package-lock.json and a .dockerignore file).

2. **Generate the Lock File (On Your Local Machine):** If you don't find a package-lock.json file in your folder, run the below command on your local,
    
    ```
    npm install
    ```
    You will see a new package-lock.json file appear. (Make sure this file is **NOT** in your .dockerignore file!)

3. **Create Dockerfile:**

    **Step 1:** The Basics (FROM and WORKDIR): Start the Dockerfile with the base image and define the working directory.
   
   Dockerfile
   ```
   FROM node:18-slim
   WORKDIR /usr/src/app
   ```
   **Step 2:** Dependencies (COPY and RUN): Copy the dependency file first and install, leveraging the build cache.

   Dockerfile
   ```
   COPY package.json package-lock.json ./
   RUN npm install
   ```
   **Step 3:** App Code and Expose: Copy the application code and expose the port (e.g., 3000).

   Dockerfile
   ```
   COPY . .
   EXPOSE 3000
   ```
   **Step 4:** The Command (CMD): Define the startup command.

   Dockerfile
   ```
   CMD ["npm", "start"]
   ```
        
5. **Build:** Execute the build command: 
   ```
   docker build -t my-web-app:1.0 .
   ```
        
6. **Run the app:** Run the container, mapping the port: 
    
   ```
   docker run -d --name my-node-app -p 8080:3000 my-web-app:1.0
   ```

7. **Test & Verify:** Test the app in the browser.

   ```
   localhost:8080
   ```
   
8. **Cleanup:** Stop and remove the container:

   ```
   docker stop my-node-app && docker rm my-node-app 
   ```
