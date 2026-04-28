#!/bin/bash

# Delete the Cluster
k3d cluster delete scientific-cluster
# Stop the cluster
# k3d cluster stop scientific-cluster

# Build the image
docker build -t thermakube-solver:v1 .

# Create the cluster
k3d cluster create scientific-cluster --agents 2

# Move the image from my laptop into the cluster nodes
k3d image import thermakube-solver:v1 -c scientific-cluster

# Deploy
kubectl apply -f deployment.yaml
