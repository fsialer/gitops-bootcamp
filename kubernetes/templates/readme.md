# Ejecutar

* Configurar cluster

```bash
kind create cluster --config kind.yml
```

* Aplicar yamls

```bash
kubectl apply -f redis-deployment.yaml
kubectl apply -f redis-service.yaml
kubectl apply -f app-deployment.yaml
kubectl apply -f app-service.yaml
```

* Checar salida

```bash
curl -v http://localhost:8080
```