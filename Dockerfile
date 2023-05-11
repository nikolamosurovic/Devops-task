FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
RUN pip install -r requirements.txt
COPY ./main.py /app

CMD ["uvicorn", "main:app", "--reload"]
