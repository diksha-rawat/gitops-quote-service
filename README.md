🎵 GitOps Quote Service
This is a simple Flask-based microservice that returns a random quote when accessed via an API endpoint. The project demonstrates how to containerize a Python app using Docker and deploy it to a local Kubernetes cluster using Minikube. It follows GitOps principles by keeping all infrastructure and app definitions in version control.

🚀 Features
REST API endpoint to fetch a random quote.

Dockerized Flask application.

Kubernetes manifests for deployment and service.

GitOps-compatible structure.

Easily extendable for CI/CD and GitOps tools like ArgoCD.

🛠️ Technologies Used
Python 3

Flask

Docker

Kubernetes

Minikube

📁 Project Structure
bash
Copy
Edit
.
├── app.py
├── Dockerfile
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── k8s
    ├── deployment.yaml
    └── service.yaml
🧪 Running the App
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/diksha-rawat/gitops-quote-service.git
cd gitops-quote-service
2. (Optional) Create a Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Flask App
bash
Copy
Edit
python app.py
🐳 Run with Docker
1. Build Docker Image
bash
Copy
Edit
docker build -t flask-microservice .
2. Run Docker Container
bash
Copy
Edit
docker run -p 5000:5000 flask-microservice
☘️ Deploy on Minikube
1. Start Minikube
bash
Copy
Edit
minikube start
2. Enable Docker Environment
bash
Copy
Edit
eval $(minikube -p minikube docker-env)
3. Build Docker Image Inside Minikube
bash
Copy
Edit
docker build -t flask-microservice .
4. Apply Kubernetes Manifests
bash
Copy
Edit
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
5. Access the App
bash
Copy
Edit
minikube service quote-service
📄 .env File (Optional)
Create a .env file in the root directory if you plan to use environment variables later.

ini
Copy
Edit
# Example
APP_PORT=5000
🧾 .gitignore
bash
Copy
Edit
venv/
__pycache__/
.env
👩‍💻 Author
Diksha Rawat — Passionate about DevOps and building scalable automation pipelines.

📜 License
This project is licensed under the MIT License.