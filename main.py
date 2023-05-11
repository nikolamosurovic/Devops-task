import json
from fastapi import FastAPI
from fastapi_lambda import FastAPILambdaHandler
from fastapi_prometheus import metrics, PrometheusMiddleware

app = FastAPI()
app.add_middleware(PrometheusMiddleware)

@app.get("/app")
def read_root():
    return {"message": "Hello from Things Solver!"}

@app.get("/app/metrics")
def read_metrics():
    return metrics()

handler = FastAPILambdaHandler(app)
lambda_handler = handler.lambda_handler()
