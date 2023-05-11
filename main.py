import json
from typing import Union
from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI()

counter = Counter("app_requests_total", "Total number of requests")

@app.get("/")
def read_root():
    counter.inc()
    return {"message": "Hello from Things Solver!"}

@app.get("/metrics")
def read_metrics():
    headers = {"Content-Type": CONTENT_TYPE_LATEST}
    return generate_latest(), headers
