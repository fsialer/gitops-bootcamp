from fastapi import FastAPI
import redis
import os

app = FastAPI()

redis_host = os.getenv("REDIS_HOST", "127.0.0.1")

# Conectar con Redis
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.get("/")
def index():
    r.incr("counter")  # Incrementar el contador en Redis
    count = r.get("counter") # Obtener el contador
    return {"message": f"¡Hola, mundo desde FastAPI en Kubernetes!, eres la visita número {count}"}
