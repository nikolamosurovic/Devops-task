# Documentation:

Transferring a Lambda Function to FastAPI Docker Service with Prometheus and Grafana Monitoring


# Requirements:

Before starting the task, ensure that you have the following software installed on your system:

   Docker: Used for containerization and building Docker images.
   
   Docker Compose: Used for defining and running multi-container Docker applications.
   
   A code editor: You can use any code editor of your choice. Example IntelliJ like me.
   
## Step 1: Transfer Lambda Function to FastAPI Docker Services

1.1. Open your code editor and create a new file named handler.py.

1.2. Write the necessary code for the Lambda function in the handler.py file. This code will be transferred to the FastAPI application.

1.3. Next, create a new file named Dockerfile in the same directory as handler.py.

1.4. Open the Dockerfile and define the instructions to build the Docker image for your FastAPI application.


## Step 2: Put the Docker Service in Docker Compose

2.1. Create a new file named docker-compose.yml in the project directory.

2.2. Open the docker-compose.yml file and define a service for your FastAPI application using the Docker image you created in the previous step.

## Step 3: Expose App Metrics with Prometheus and Grafana

3.1. Add Prometheus and Grafana as additional services in the docker-compose.yml file. 

3.2. Create a prometheus directory and prometheus.yml file in that directory. This file will define the Prometheus configuration. 


## Step 4: Create Grafana Dashboard with Exposed Metrics

4.1. Open your web browser and access Grafana at http://localhost:3000.

4.2. Log in to Grafana using the default credentials (admin/admin).

4.3. Configure Prometheus as a data source in Grafana:

- Click on the "Home" icon on the left sidebar and select "Data Sources".
- Click on "Add new data source" and select Prometheus.
- Configure the data source with the following settings:
- Name: Prometheus
- URL: http://prometheus:9090
- Save and Test the configuration.

4.4. Create a new dashboard in Grafana:

- Click on the "+" icon on the left sidebar and select "Dashboard" -> "New Dashboard".
- Click on "+ Add visualization"
- Configure the graph with the following settings:
- Metrics: Select the appropriate metric for total memory consumption. In this case, use this metric: cointainer_memory_usage_bytes
- Select labels: cadvisorRevision
- For network traffic, repeat this steps, just replace cointainer_memory_usage_bytes with cointainter_network_transmit_bytes_total

## Step 5: Run Docker Compose to Bring Everything Up

5.1. Open a terminal or command prompt and navigate to the project directory.

5.2. Run the command docker-compose up to start the containers defined in the docker-compose.yml file.

5.3. Wait for the containers to start and for the application to be accessible.

5.4. Access the FastAPI application at http://localhost:8000 to verify that it is running correctly.

5.5. Access Prometheus at http://localhost:9090 to verify that it is running correctly. On the Status-Targets page, you should see the CAAdvisor metrics up.

5.6. Access the Grafana dashboard at http://localhost:3000 and navigate to the created dashboard to view the metrics.
