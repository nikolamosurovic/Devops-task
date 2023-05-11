import json
from fastapi import FastAPI
from fastapi_lambda import FastAPILambdaHandler
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"message": "Hello from Things Solver!"}

handler = FastAPILambdaHandler(app)
lambda_handler = handler.lambda_handler()
