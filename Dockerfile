FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./main.py /app

CMD ["uvicorn", "main:app", "--reload"]
