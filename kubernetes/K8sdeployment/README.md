## Deploy any application step by step using local docker/minikube(k8s)

<br>
1.Make ur API ready and test it locally </br> 
2.Keep the poetry file ready for environment </br> 
3.Build docker image and run it to test it </br> 
4.Start minikube and deploy it in k8s single cluster </br> 
5.Make deployment and service files and redeploy in k8s </br> 
6.Use helm to handle deployment templates </br> 
7.Try it out in GCP </br> 
</br>

<b>Steps:</b></br></br>
Before we build the image, if we want to use gpu inside docker container, we need to install nvidia-docker-toolkit. Please follow the instructions here for installation</br>

https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker
</br>

once we are done with the above installation, we can check the __nvidia-smi__ command inside the container by the running the following command

```
docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
```

Note: the above image is from dockerhub nvidia-base. we can have our custom image with nvidia/cuda base


To build the image run the below command:
``` 
docker build --tag <dockerhubname>/<projname>:<tag> .
```

Run the below command for starting the container with gpu access. Also, we just need to have nvidia driver installed in our local. we dont need cuda toolkit in our local, it will be handled by the image itself


<img src="https://cloud.githubusercontent.com/assets/3028125/12213714/5b208976-b632-11e5-8406-38d379ec46aa.png" alt="alt text" title="image Title" />



```
docker run --rm --name <container name> -p 8000:8000 --gpus all <REPOSITORY>:<TAG>
```

To push the image to dockerhub

```
docker push <REPOSITORY>:<TAG>
```


### Start minikube

Downloads minikube image from gcr and start minikube

```
minikube start
```

Check the cluster info
```
kubectl cluster-info
```

Now we can create deployment using CLI and also using files. 

First, we will run the deployments using cli

```
kubectl create deployment <deployment name> --image=<REPOSITORY>:<TAG>
```

To check the status of deployment
```
kubectl get deployment
```

Rollout the deployment to create pods with the below command
```
kubectl rollout status deployment <deployment name>
```

To check the pod status
```
kubectl get pods
```

Next, we need to expose the deployment for making it available outside

```
kubectl expose deployment <deployment name> --port 5000 --type=LoadBalancer
```
To check service status

```
minkube service list
```

Note:
Neither Docker Desktop or Minikube setup a real-life load balancer.


To tear-down the load balancer, deployment and pod, run the following commands in sequence,

```
kubectl delete deployment <deployment name>
kubectl delete service <service name>
```

Now, we will create deployments using yaml files


```
kubectl apply -f deployment.yaml
```

<b>Note:</b></br>
we have defined three separate Kubernetes components in this single file: a namespace, a deployment and a load-balanced service - for all of these components (and their sub-components), using --- to delimit the definition of each separate component. To see all components deployed into this namespace use,

```
kubectl get all --namespace <namespace name>
```

To list the pods deployed 
```
kubectl get pods --all-namespaces
```

Now, we will proceed with using helm to manage yaml templates. Install helm using the following link https://docs.helm.sh/docs/intro/install/.


Helm relies on a dedicated deployment server, referred to as the ‘Tiller’, to be running within the same Kubernetes cluster we wish to deploy our applications to. Before we deploy Tiller we need to create a cluster-wide super-user role to assign to it, so that it can create and modify Kubernetes resources in any namespace. 

```
kubectl --namespace kube-system create serviceaccount tiller

kubectl create clusterrolebinding tiller \
    --clusterrole cluster-admin \
    --serviceaccount=kube-system:tiller
```

Now,create a helm and modify the templates and install it

The below cmd will create helm folders and default templates which has to be modified for custom usecases
```
helm create <helm name>
```
After making changes we can run the below cmd to do a dry run and verify

```
helm install <helm name> --debug --dry-run --generate-name
```

Post which we can do the actual deployment

```
helm install <helm name> --generate-name
```

Now, we can check deployed namespaces or services using the commands to see the deployed resources. Stop the minikube service

```
minikube stop
```


