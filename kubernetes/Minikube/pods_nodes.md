## Kubernetes Pods & Services

<br>
Pods are the atomic unit on the Kubernetes platform. When we create a Deployment on Kubernetes, that Deployment creates Pods with containers inside them.
</br>

<br>
<b>kubectl get</b> - list resources</br>
<b>kubectl describe</b> - show detailed information about a resource</br>
<b>kubectl logs</b> - print the logs from a container in a pod</br>
<b>kubectl exec</b> - execute a command on a container in a pod</br>

<br>
Although each Pod has a unique IP address, those IPs are not exposed outside the cluster without a Service. Services allow your applications to receive traffic. Services can be exposed in different ways by specifying a type in the ServiceSpec:
</br>

<br>
<b>ClusterIP (default)</b> - Exposes the Service on an internal IP in the cluster. This type makes the Service only reachable from within the cluster.</br>
<b>NodePort</b> - Exposes the Service on the same port of each selected Node in the cluster using NAT. Makes a Service accessible from outside the cluster using NodeIP:NodePort. Superset of ClusterIP.</br>
<b>LoadBalancer</b> - Creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP to the Service. Superset of NodePort.</br>
<b>ExternalName</b> - Maps the Service to the contents of the externalName field (e.g. foo.bar.example.com), by returning a CNAME record with its value. No proxying of any kind is set up.
</br>


<br>
<b>kubectl get pods -l app=kubernetes-bootcamp</b> list pods matching that label</br>
<b>kubectl label pods $POD_NAME version=v1 </b> adds new labels to the pods

<br>
We created a Deployment, and then exposed it publicly via a Service. The Deployment created only one Pod for running our application. When traffic increases, we will need to scale the application to keep up with user demand.

Scaling is accomplished by changing the number of replicas in a Deployment
</br>

<br>
<b>kubectl get rs</b> - Get replica set</br>
<b>kubectl scale deployments/kubernetes-bootcamp --replicas=4 </b> - scale the pods to 4</br>

<br>
Rolling updates allow Deployments' update to take place with zero downtime by incrementally updating Pods instances with new ones. </br>

<br>
<b>
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2</b> - Updates new image</br>
<b>kubectl rollout status deployments/kubernetes-bootcamp</b> - Check the rollout status</br>
<b>kubectl rollout undo deployments/kubernetes-bootcamp</b> - Undo the rolledout application</br>