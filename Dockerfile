FROM python:3.9-slim

WORKDIR /app

COPY script/ /app/script/
COPY data/ /app/data/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python /app/script/main.py