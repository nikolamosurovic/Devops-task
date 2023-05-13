# Use an official Python runtime as the base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Set the working directory to /app
WORKDIR /app

# Install Unicorn and FastAPI
RUN pip install uvicorn fastapi

# Copy the Lambda function code into the container
COPY handler.py .

# Expose the FastAPI port (change it if necessary)
EXPOSE 8000

# Set the CMD to your Lambda handler
CMD ["uvicorn", "handler:app", "--host", "0.0.0.0"]