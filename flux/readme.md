# Crear cluster

```bash
kind create cluster --config kind.yml
```

# Install flux

```bash
curl -s https://fluxcd.io/install.sh | sudo bash
```

* Checar

```bash
flux check --pre
```

* Crear controladores

```bash
flux install
```

* Checar recursos creados en el namespace

```bash
kubectl get pods -n flux-system
```

* Exportar github token

```bash
export GITHUB_TOKEN=
export GITHUB_USER=
```

* Configurar flux con github

```bash
flux bootstrap github \
  --owner=$GITHUB_USER \
  --repository=gitops-bootcamp \
  --branch=main \
  --path=./flux/templates \
  --personal
```