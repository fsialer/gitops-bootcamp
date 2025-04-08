# How to install

```bash
kubectl create namespace argocd
```

```bash
kubectl apply -n argocd -f  https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

```bash
kubectl get deployments -n argocd
```

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 --decode
```