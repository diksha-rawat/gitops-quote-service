# GitOps Quote Service 📝

This is a simple Flask-based microservice that returns a random quote via a REST API. It is designed to be containerized using Docker and deployed to a Kubernetes cluster using GitOps principles with ArgoCD and Helm.

Features:
- REST API with one endpoint: /quote
- Returns a random quote in JSON format
- Lightweight and ideal for microservice demonstration
- Ready for CI/CD and GitOps pipeline

Getting Started:

Prerequisites:
- Docker
- Python 3.8+
- Flask (install via `pip install -r requirements.txt`)

Run Locally:
1. Install requirements: `pip install -r requirements.txt`
2. Run the app: `python app.py`

Run with Docker:
1. Build the image: `docker build -t flask-microservice .`
2. Run the container: `docker run -p 5000:5000 flask-microservice`

Sample Output:
{
  "quote": "The only limit to our realization of tomorrow is our doubts of today."
}

To Do:
- Add more quotes and categories
- Add health check endpoint
- Create Helm chart
- Deploy via ArgoCD

Contributing:
PRs and improvements are welcome!

License:
MIT License