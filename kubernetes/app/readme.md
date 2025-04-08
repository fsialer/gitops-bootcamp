# Instalar

* Crear entorno virtual

```bash
python3 -m venv venv
```

* Activar entorno
```bash
source venv/bin/activate
```

* Instalar depedencias
```bash
pip install -r requirements.txt
```

* Ejecutar app
```bash
uvicorn main:app --reload
```

* Validar salida

```bash
curl -v http://localhost:8000
```

# Ejecutar con Docker

* Para crear imagen de Docker

```bash
docker build -t fastapi .
```

* Ejecutar docker compose

```bash
docker compose up -d
```