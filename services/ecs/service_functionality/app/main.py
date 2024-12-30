from fastapi import FastAPI
import socket

app = FastAPI()


@app.get("/get-ip")
def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    return {
        "ip": ip_address
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }
