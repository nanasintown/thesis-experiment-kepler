#!/bin/bash


kubectl apply -f workload-deployment.yaml

#get pods/resource
kubectl get all -n workload

kubectl get pods -n workload
