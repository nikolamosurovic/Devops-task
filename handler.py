import json
from fastapi import FastAPI
import psutil
from prometheus_client import CollectorRegistry, Gauge, generate_latest

memory_usage = Gauge('memory_usage', 'Total memory usage in bytes')
app=FastAPI()

@app.get("/")
def lambda_handler():
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Things Solver!')
    }
