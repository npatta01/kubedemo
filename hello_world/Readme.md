
# Hello World (python)

## Description
A simple python flask web app.



## Pre docker

```
python app.py
```

Were there issues ?

Missing package
```
pip3 install -r requirements.txt
```

Python 3 Env
```
sudo apt-get install -y --no-install-recommends python3-pip
pip3 install Flask==0.12
```



## Docker 

Setup
```
USER=$(whoami)
export PROJECT_ID=$(gcloud config get-value project -q)
```

Build your image
```
docker build -t gcr.io/${PROJECT_ID}/pythonhello-${USER}:latest .
```


Run your image
```
docker run --rm -p 5000:5000 gcr.io/${PROJECT_ID}/pythonhello-${USER}:latest
 
```

Store your image in Google Container Registry
```
gcloud docker -- push gcr.io/${PROJECT_ID}/pythonhello-${USER}:latest
```

Verify image exists
```
gcloud container images list-tags gcr.io/${PROJECT_ID}/pythonhello-${USER}:latest .
```


### Fun things to do

Run container
```
docker run -p 5000:5000 gcr.io/${PROJECT_ID}/pythonhello-${USER}:latest
```

View running containers
```
docker ps 
```

View Logs
```
docker logs {containerid} -f
```

SSH to container
```
docker exec -it {containerid} /bin/bash
```

Delete files
```
rm -rf *
```

Run container
```
#gcloud docker -- pull gcr.io/${PROJECT_ID}/pythonhello-${USER}:latest
gcloud docker -- run gcr.io/${PROJECT_ID}/pythonhello-${USER}:latest -p 5000:5000
```

Depploy app on Now
```
sudo npm install -g now   
now      
now --public   
```

Deploy app on Heroku
```
wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh
heroku container:login
heroku create {project-name}
heroku container:push web
heroku open
```



## Kubernetes

List all available clustes
```
gcloud container clusters list --zone us-east1-b
```

Get credentials needed to talk to kube cluster
```
CLUSTER_NAME=dataapps
gcloud container clusters get-credentials ${CLUSTER_NAME} --zone us-east1-b 
```

Get all pods
```
kubectl get pods
```

Get all deploymets
```
kubectl get deploymets
```

Get all service
```
kubectl get svc
```

Get all  ingress resources
```
kubectl get ing
```

deploy our application
```
kubectl appply -f k8s/deployment.yaml
kubectl appply -f k8s/service.yaml

```

Get endpoints of our service
```
kubectl get endpoints {servicename}
```


### Ingress Notes
Reserve an ip for our load balancer
```
IP_NAME=k8s-global-ip-demo
gcloud compute addresses create ${IP_NAME} --global
```

Verify ip is setup
```
gcloud compute addresses list
```

The ip name is specified in the ingress file under "kubernetes.io/ingress.global-static-ip-name".

A DNS A record needs to be created for the new load balancer

Deploy the ingress
```
kubectl apply -f k8s/ingress.yaml
```
