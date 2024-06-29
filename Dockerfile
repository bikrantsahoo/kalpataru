FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y build-essential libssl-dev libffi-dev python3-dev libpq-dev
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
