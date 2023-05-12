# Use an official Python runtime as the base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Set the working directory to /app
WORKDIR /app

# Install Unicorn and FastAPI
RUN pip install uvicorn fastapi prometheus-client psutil

# Copy the Lambda function code into the container
COPY handler.py .

# Set the CMD to your Lambda handler (modify as needed)
CMD ["uvicorn", "handler:app", "--host", "0.0.0.0"]