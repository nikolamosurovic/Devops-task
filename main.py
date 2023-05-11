import json
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def lambda_handler():
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Things Solver!')
    }