FROM python:3.10.9-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

CMD ["python", "bot.py"]

