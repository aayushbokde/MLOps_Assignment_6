# ML Model Deployment with CI/CD (GitHub Actions + DockerHub)

## 📌 Overview
This project demonstrates a **CI/CD pipeline** for a simple ML model (Logistic Regression on Iris dataset).  
The pipeline trains the model, serves it via Flask API, and deploys the app as a Docker container image.  

## ⚙️ Pipeline Stages
1. **Install dependencies**  
2. **Train model** → saves `model.pkl`  
3. **Run tests**  
4. **Build Docker image**  
5. **Push Docker image to DockerHub**  
6. **Deploy (simulated)**  

## 🚀 Deployment
The Docker image is automatically pushed to **DockerHub**.  

You can pull and run it locally:
```bash
docker pull <your-dockerhub-username>/ml-model-app:latest
docker run -p 8000:8000 <your-dockerhub-username>/ml-model-app:latest
