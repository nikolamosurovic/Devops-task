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


@app.get("/metrics")
def generate_prometheus_metrics():
    # Get total memory usage
    memory_stats = psutil.virtual_memory()
    total_memory_usage = memory_stats.total

    # Set the metric value
    memory_usage.set(total_memory_usage)

    # Create a new registry
    registry = CollectorRegistry()

    # Register the metric with the registry
    registry.register(memory_usage)

    # Generate the Prometheus text format
    metrics = generate_latest(registry)

    # Return the metrics as the response
    print (metrics.decode('utf-8'))
    return metrics.decode('utf-8')