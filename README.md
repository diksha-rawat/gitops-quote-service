# 🎵 GitOps Quote Service

A Flask-based microservice that returns a random quote via an API. This project showcases how to containerize a Python app using Docker and deploy it to a local Kubernetes cluster using Minikube. It follows GitOps principles by version-controlling both infrastructure and application code.

---

## 🚀 Features

- ✨ REST API endpoint to fetch random quotes  
- 🐳 Dockerized Flask application  
- ☸️ Kubernetes manifests for deployment and service  
- 🧾 GitOps-friendly directory structure  
- 🔧 Easily extensible for CI/CD and GitOps tools like ArgoCD  

---

## 🛠️ Technologies Used

- Python 3  
- Flask  
- Docker  
- Kubernetes  
- Minikube  

---

## 📁 Project Structure

```
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
```

---

## 🧪 Running the App Locally

### 1. Clone the Repository
```bash
git clone https://github.com/diksha-rawat/gitops-quote-service.git
cd gitops-quote-service
```

### 2. (Optional) Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask App
```bash
python app.py
```

---

## 🐳 Run with Docker

### 1. Build Docker Image
```bash
docker build -t flask-microservice .
```

### 2. Run Docker Container
```bash
docker run -p 5000:5000 flask-microservice
```

---

## ☘️ Deploy on Minikube

### 1. Start Minikube
```bash
minikube start
```

### 2. Configure Docker Environment for Minikube
```bash
eval $(minikube -p minikube docker-env)
```

### 3. Build Docker Image Inside Minikube
```bash
docker build -t flask-microservice .
```

### 4. Apply Kubernetes Manifests
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 5. Access the App
```bash
minikube service quote-service
```

---

## 🔐 Environment Configuration (`.env` file)

Create a `.env` file in the project root if you want to configure variables:

```env
# Example
APP_PORT=5000
```

---

## 📄 .gitignore

```gitignore
venv/
__pycache__/
.env
```

---

## 👩‍💻 Author

**Diksha Rawat**

---

## 📜 License

This project is licensed under the MIT License.