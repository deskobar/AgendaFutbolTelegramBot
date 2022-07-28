FROM python:3.10

WORKDIR /app

COPY * .

RUN pip install requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]

EXPOSE 8080