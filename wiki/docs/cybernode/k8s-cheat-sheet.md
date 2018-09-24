# K8s cheat sheet

## k8s dashboard
Local dashboard proxy:
```bash
kubectl proxy
```
Get cluster access token:
```bash
kubectl config view | grep -A10 "name: $(kubectl config current-context)" | awk '$1=="access-token:"{print $2}'
```
Get logs of previously running container (if it failed and then restarts):
```bash
kubectl logs mypod --previous
```
## Reset GKE Node
```bash
gcloud compute instances reset gke-kubia-default-pool-b46381f1-zwko
```
## Forward pod port on localhost
```bash
kubectl port-forward -n monitoring prometheus-kube-prometheus-0 9090
```

Forward port of first found pod with specific namespace and label: 
```bash
kubectl port-forward -n chains $(kubectl get pod -n chains -l chain=bitcoind-btc -o jsonpath="{.items[0].metadata.name}") 8332
```
## Elassandra commands
Get nodes status:
```bash
kubectl exec -n search elassandra-0 -- nodetool status
```
Open cqlsh CLI tool
```bash
kubectl exec -it -n search elassandra-0 -- cqlsh
```
Dive into elassandra docker container shell(index stats, delete index commands examples)
```bash
kubectl exec -n search -it elassandra-0 bash
curl -XGET 'localhost:9200/_cat/indices?v&pretty'
curl -XDELETE 'localhost:9200/twitter?pretty'
```