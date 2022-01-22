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

