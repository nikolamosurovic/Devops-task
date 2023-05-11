import json
from fastapi import FastAPI
from fastapi_lambda import FastAPILambdaHandler
from fastapi_prometheus import metrics, PrometheusMiddleware

app = FastAPI()
app.add_middleware(PrometheusMiddleware)

@app.get("/")
def read_root():
    return {"message": "Hello from Things Solver!"}

@app.get("/metrics")
def read_metrics():
    return metrics()

handler = FastAPILambdaHandler(app)
lambda_handler = handler.lambda_handler()
