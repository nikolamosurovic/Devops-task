import json
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

@app.get("/lambda")
def lambda_handler():
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Things Solver!')
    }

@app.get("/metrics")
def get_metrics():
    return {"message": "Metrics endpoint"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
