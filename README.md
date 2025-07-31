# 🧠 GitOps Quote Service

A simple Flask microservice that returns a random motivational quote. Designed as a DevOps-ready application to demonstrate containerization, Kubernetes deployment, and GitOps principles.

---

## 🚀 Features

- Flask REST API  
- Random quote generator  
- Dockerized for easy deployment  
- Kubernetes manifests for deployment  
- Minikube setup for local testing  
- GitOps-friendly project structure  

---

## 📁 Project Structure

gitops-quote-service/
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
├── k8s-manifests/
│ ├── deployment.yaml
│ └── service.yaml

yaml
Copy
Edit

---

## 🧪 Local Development

### Prerequisites

- Python 3.8+
- `pip`
- Docker

### Install dependencies

```bash
pip install -r requirements.txt
Run locally
bash
Copy
Edit
python app.py
🐳 Run with Docker
Build Docker image
bash
Copy
Edit
docker build -t flask-microservice .
Run container
bash
Copy
Edit
docker run -p 5000:5000 flask-microservice
Visit: http://localhost:5000/quote

☸️ Deploy to Kubernetes using Minikube
Step 1: Start Minikube
bash
Copy
Edit
minikube start
If you get a segmentation fault or want to use Docker driver:

bash
Copy
Edit
minikube start --driver=docker
Step 2: Enable Docker environment for Minikube (optional)
bash
Copy
Edit
eval $(minikube docker-env)
docker build -t flask-microservice .
Step 3: Apply Kubernetes manifests
bash
Copy
Edit
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
Step 4: Access the service
bash
Copy
Edit
minikube service flask-service
This will open the app in your default browser. If the service name is different, replace flask-service accordingly.

🛠️ GitOps Ready
This project is structured to support GitOps workflows using tools like ArgoCD or Flux. Kubernetes manifests are kept declaratively under the k8s/ directory.

📜 License
MIT License

💡 Author
Diksha Rawat

vbnet
Copy
Edit

Let me know when you want to add CI/CD or ArgoCD GitOps deployment steps.