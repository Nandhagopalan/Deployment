## Kubernetes cluster components

<br>
When you deploy Kubernetes, you get a cluster. A Kubernetes cluster consists of a set of worker machines, called nodes, that run containerized applications. Every cluster has at least one worker node.
</br>

<br>
The worker node(s) host the Pods that are the components of the application workload. The control plane manages the worker nodes and the Pods in the cluster. In production environments, the control plane usually runs across multiple computers and a cluster usually runs multiple nodes, providing fault-tolerance and high availability.
</br>

<br>
<img src="https://d33wubrfki0l68.cloudfront.net/2475489eaf20163ec0f54ddc1d92aa8d4c87c96b/e7c81/images/docs/components-of-kubernetes.svg" alt="alt text" title="image Title" />
</br>

## Control Plane Components:

The Control Plane is responsible for managing the cluster. 

<b>Kube-apiserver:</b>

The API server is a component of the Kubernetes control plane that exposes the Kubernetes API. The API server is the front end for the Kubernetes control plane.

<b>etcd:</b>

Consistent and highly-available key value store used as Kubernetes' backing store for all cluster data.

<b>kube-scheduler:</b>
Control plane component that watches for newly created Pods with no assigned node, and selects a node for them to run on.

## Node Components:

Node components run on every node, maintaining running pods and providing the Kubernetes runtime environment.

<b>kubelet:</b>
An agent that runs on each node in the cluster. It makes sure that containers are running in a Pod.

<b>kube-proxy</b>
kube-proxy is a network proxy that runs on each node in your cluster, implementing part of the Kubernetes Service concept.

kube-proxy maintains network rules on nodes. These network rules allow network communication to your Pods from network sessions inside or outside of your cluster.