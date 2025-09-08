# Flask Microservice with Docker and Kubernetes

A RESTful API microservice built with Flask, containerized with Docker, and deployed to Kubernetes with a CI/CD pipeline using GitHub Actions.

## Features

* RESTful API with CRUD operations
* Docker containerization
* Kubernetes deployment with auto-scaling
* CI/CD pipeline with GitHub Actions
* Automated testing with pytest

## API Endpoints

* `GET /` - Health check and API info
* `GET /api/items` - Get all items
* `POST /api/items` - Create a new item
* `GET /api/items/<id>` - Get a specific item
* `PUT /api/items/<id>` - Update an item
* `DELETE /api/items/<id>` - Delete an item

### Sample curl Requests

```bash
# Health check
curl http://localhost:5000/

# Get all items
curl http://localhost:5000/api/items

# Create a new item
curl -X POST http://localhost:5000/api/items -H 'Content-Type: application/json' -d '{"name":"Test Item","description":"A test item"}'

# Get a specific item
curl http://localhost:5000/api/items/<item_id>

# Update an item
curl -X PUT http://localhost:5000/api/items/<item_id> -H 'Content-Type: application/json' -d '{"name":"Updated Item"}'

# Delete an item
curl -X DELETE http://localhost:5000/api/items/<item_id>
```

## Local Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `flask run`
4. Run tests: `pytest`

## Docker

Build the image:

```bash
docker build -t flask-microservice .
```

Run the container:

```bash
docker run -p 5000:5000 flask-microservice
```

Or use Docker Compose:

```bash
docker-compose up --build
```

## Kubernetes Deployment

### Using Minikube (local cluster)

```bash
minikube start
kubectl apply -f k8s/
minikube service flask-microservice-service
```

### Using AWS EKS (cloud)

1. Update image in `k8s/deployment.yaml` with your DockerHub username.
2. Configure AWS CLI and EKS cluster:

```bash
aws eks --region <your-region> update-kubeconfig --name <your-cluster>
```

3. Apply manifests:

```bash
kubectl apply -f k8s/
```

4. Get external service URL:

```bash
kubectl get svc flask-microservice-service
```

## CI/CD with GitHub Actions

* Workflow: `.github/workflows/ci-cd.yaml`
* On every push to `main`:

  1. Runs tests with **pytest**
  2. Builds and pushes Docker image to **DockerHub**
  3. Deploys to **Kubernetes (EKS)**

### Required GitHub Secrets

* `DOCKERHUB_USERNAME`
* `DOCKERHUB_TOKEN`
* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
* `AWS_REGION`
* `EKS_CLUSTER_NAME`

## Instructions to Run

1. Extract the ZIP file
2. Install Python dependencies: `pip install -r requirements.txt`
3. Run the application locally: `python app/main.py`
4. Run tests: `pytest`
5. Build Docker image: `docker build -t flask-microservice .`
6. Run with Docker: `docker run -p 5000:5000 flask-microservice`
7. For Kubernetes deployment, update the image references in the YAML files
8. Set up the required secrets in GitHub for the CI/CD pipeline
