FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./main.py /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]