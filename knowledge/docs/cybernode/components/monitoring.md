# Monitoring Components

During lifetime cybernode collects various metrics using following components:

| Component               | Description                                      |  Cluster Address               | External |
| ----------------------- | ------------------------------------------------ | ------------------------------ | -------- |
| Prometheus Operator(PO) | Manages Prometheus Configuration                 |                                |          |
| Prometheus              | Metrics Storage                                  | prometheus.monitoring.svc:9090 |          |
| Default Service Monitor | Default Service Monitor for PO                   |                                |          |
| Grafana                 | Metrics Alerts and Web UI                        | grafana.monitoring.svc:3000    |    y     |


## Prometheus

[Prometheus](https://prometheus.io/) is used as a main metrics storage. Components collect metrics and expose them via 
 HTTP endpoint, that Prometheus pulls at configured interval(our is 15s).
 
### Prometheus Operator
To deploy Prometheus atop Kubernetes, we use [Prometheus Operator](https://coreos.com/operators/prometheus/docs/latest/).
 It consists of Prometheus Operator itself, that introduced to cluster 
 [CRDs](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/): Prometheus,
 Service Monitor. PO automatically(dynamically) generate monitoring target configurations based on familiar Kubernetes label queries; 
 no need to learn a Prometheus specific configuration language.
 
### Default Service Monitor
To enable dynamic mapping for new pods to prometheus, service monitor(SM) is used. Each SM defines set of kubernetes 
 label filters.

## Grafana
To visualize metrics collected by Prometheus we use [Grafana](https://grafana.com/). In order to configure Grafana, three
 [config maps](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) are used:
 
1. **grafana-datasources**. Define Prometheus datasource. 
2. **grafana-dashboards**. Gather predefined dashboards into single folder. 
3. **grafana-dashboards-providers**. Configuration for importing dashboards. 

### Grafana Alerts
Also Grafana supports checking metrics satisfied defined criteria. If criteria is violated, than notification is raised 
 to setup alert channels(in our case Telegram Group). To view list of available alerts check 
 "{grafana_host}/alerting/list" page. 