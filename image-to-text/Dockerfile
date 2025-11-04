# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# 1. Install Tesseract OCR and its dependencies
# The 'tesseract-ocr' package provides the Tesseract executable
# The 'libtesseract-dev' provides the headers needed for pytesseract
RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev && \
    rm -rf /var/lib/apt/lists/*

# 2. Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Create the templates directory and copy the HTML file into it
RUN mkdir templates
COPY index.html templates/

# 4. Copy the application code
COPY app.py .

# Expose the port the app runs on
EXPOSE 5000

# Run the application using Flask's simple server
CMD ["flask", "run", "--host=0.0.0.0"]