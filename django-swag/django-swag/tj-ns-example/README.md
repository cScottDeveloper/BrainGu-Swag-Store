```bash
kubectl apply -k . # Deploy example NGINX pods to cluster. Each pod in it's own namespace. Expose pod 2 with a ClusterIP Service so it is accessible from Pod 1 in Namespace 1.

kubectl exec -it -n one one sh
curl one/ # Notice successful curl due to hostname redirection to localhost
curl two/ # Notice failure due to inability to resolve hostname

curl two.two.svc.cluster.local # Notice ability to curl pod in other namespace via exposed ClusterIP service using FQDN
exit
kubectl delete -k . # Clean up the example app
```
