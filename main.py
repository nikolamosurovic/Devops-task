import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Things Solver!')
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

