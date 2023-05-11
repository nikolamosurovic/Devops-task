import json
from fastapi import FastAPI
from fastapi_prometheus import metrics, PrometheusMiddleware

app = FastAPI()

app.add_middleware(PrometheusMiddleware)

@app.get("/")
def read_root():
    return {"message": "Hello from Things Solver!"}

@app.get("/metrics")
def read_metrics():
    return metrics()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
