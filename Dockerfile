FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY config.yaml .

HEALTHCHECK --interval=10s --timeout=3s \
  CMD python -c "from src.health import health_check; import sys; sys.exit(0 if health_check()['status']=='ok' else 1)"

CMD ["python", "src/main.py"]
