from fastapi import FastAPI
import socket
import time
import psutil

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

@app.get("/simulate-cpu")
def simulate_cpu():
    cpu_utilization = psutil.cpu_percent(interval=1)
    fake_list = []

    while cpu_utilization < 50:
        try:
            print(cpu_utilization)
            fake_list.extend([x**2 for x in range(1000000)])
            cpu_utilization = psutil.cpu_percent(interval=1)
        except Exception as e:
            print(e)
            break

    return {
        "status": "CPU utilization simulated",
        "cpu_utilization": cpu_utilization
    }
