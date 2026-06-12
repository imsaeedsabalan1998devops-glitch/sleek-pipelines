import requests
import time
import csv
import os
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [LATENCY] %(message)s"
)

TARGET_URL = "http://localhost:8000/health"
OUTPUT_FILE = "latency_history.csv"

def measure_latency():
    timestamp = datetime.now().isoformat()

    try:
        start = time.time()
        response = requests.get(TARGET_URL, timeout=3)
        end = time.time()

        latency_ms = round((end - start) * 1000, 2)

        if response.status_code == 200:
            logging.info(f"Latency OK: {latency_ms} ms")
            write_csv(timestamp, latency_ms, "UP")
        else:
            logging.warning(f"Service unhealthy. Status: {response.status_code}")
            write_csv(timestamp, None, "UNHEALTHY")

    except Exception as e:
        logging.error(f"Service DOWN: {e}")
        write_csv(timestamp, None, "DOWN")

def write_csv(timestamp, latency, status):
    file_exists = os.path.isfile(OUTPUT_FILE)

    with open(OUTPUT_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "latency_ms", "status"])

        writer.writerow([timestamp, latency, status])

if __name__ == "__main__":
    measure_latency()
