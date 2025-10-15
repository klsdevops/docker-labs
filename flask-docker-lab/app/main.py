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