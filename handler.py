import json
import uvicorn
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Instrument FastAPI app
Instrumentator().instrument(app).expose(app)

@app.get("/")
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Things Solver!')
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
