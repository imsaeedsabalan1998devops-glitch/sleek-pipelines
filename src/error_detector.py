import requests
import csv
import os
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [ERROR-DETECTOR] %(message)s"
)

METRICS_URL = "http://localhost:8000/metrics"
OUTPUT_FILE = "error_events.csv"

def detect_errors():
    timestamp = datetime.now().isoformat()

    try:
        response = requests.get(METRICS_URL, timeout=3)

        if response.status_code != 200:
            logging.warning(f"Service unhealthy: {response.status_code}")
            write_csv(timestamp, "UNHEALTHY", None)
            return

        data = response.json()
        requests_count = data.get("requests", None)

        if requests_count is None:
            logging.warning("Metrics missing 'requests' field")
            write_csv(timestamp, "MISSING_FIELD", None)
            return

        logging.info(f"Requests count OK: {requests_count}")
        write_csv(timestamp, "OK", requests_count)

    except Exception as e:
        logging.error(f"Service DOWN: {e}")
        write_csv(timestamp, "DOWN", None)

def write_csv(timestamp, status, requests_count):
    file_exists = os.path.isfile(OUTPUT_FILE)

    with open(OUTPUT_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "status", "requests_count"])

        writer.writerow([timestamp, status, requests_count])

if __name__ == "__main__":
    detect_errors()
