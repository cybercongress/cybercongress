### Prerequisites

1. Install [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
for interacting with Kubernetes.

2. Install [minikube](https://github.com/kubernetes/minikube) if you want to
test setup locally. Make sure to install driver for your OS or else slow
VirtualBox will be used.


### Running `minikube` for local testing


    $ minikube start --vm-driver kvm2
    Starting local Kubernetes v1.9.0 cluster...
    Starting VM...
    Getting VM IP address...
    Moving files into cluster...
    Setting up certs...
    Connecting to cluster...
    Setting up kubeconfig...
    Starting cluster components...
    Kubectl is now configured to use the cluster.
    Loading cached images from config file.

Check status.

    $ minikube status
    minikube: Running
    cluster: Running
    kubectl: Correctly Configured: pointing to minikube-vm at 192.168.39.6

Run dashboard.

    $ minikube dashboard
    Opening kubernetes dashboard in default browser...

### Run single container in a cluster

    $ kubectl run miniecho --image=k8s.gcr.io/echoserver:1.9 --port=8080

This adds `deployment` called `miniecho` to cluster, runs Docker `echoserver`
image in it and tells docker to open port 8080. The port is not accessible
until we create `service`.

    $ kubectl expose deployment miniecho --type=NodePort
    service "miniecho" exposed

This makes `miniecho` service accessible from your machine on random port.

    $ minikube service list
    |-------------|----------------------|---------------------------|
    |  NAMESPACE  |         NAME         |            URL            |
    |-------------|----------------------|---------------------------|
    | default     | kubernetes           | No node port              |
    | default     | miniecho             | http://192.168.39.6:30426 |
    | kube-system | kube-dns             | No node port              |
    | kube-system | kubernetes-dashboard | http://192.168.39.6:30000 |
    |-------------|----------------------|---------------------------|

