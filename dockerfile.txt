FROM python:3.11-slim

WORKDIR /app

COPY pythonapp.py .

CMD ["python", "pythonapp.py"]
