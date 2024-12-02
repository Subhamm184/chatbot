Setup Instructions
1.Running with Docker
  >Clone this repository:
    git clone <repository-url>
    cd <repository-name>
  >Build the Docker image:
   docker build -t flask-app .
  >Run the Docker container:
   docker run -d -p 8080:5000 --name flask-container flask-app
  >Open your browser and go to http://localhost:8080 to access the app.

2. Running Locally (Without Docker)

  >Clone this repository:
    git clone <repository-url>
    cd <repository-name>
  >Create a virtual environment:
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
  >Install the dependencies:
    pip install -r requirements.txt
  >Run the Flask application:
    python app.py
  >Open your browser and go to
    http://127.0.0.1:5000 to access the app.
