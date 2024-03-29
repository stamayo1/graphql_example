FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY ./main.py /app/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
