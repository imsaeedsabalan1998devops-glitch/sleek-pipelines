import requests
import logging
import csv
import os
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [UPTIME-TRACKER] %(message)s"
)

METRICS_URL = "http://localhost:8000/metrics"
OUTPUT_FILE = "uptime_history.csv"

def track_uptime():
    timestamp = datetime.now().isoformat()

    try:
        response = requests.get(METRICS_URL, timeout=3)
        if response.status_code == 200:
            data = response.json()
            uptime = data.get("uptime", None)

            logging.info(f"Service is UP. Uptime: {uptime}")

            write_csv(timestamp, uptime, "UP")
        else:
            logging.warning("Service responded but not healthy.")
            write_csv(timestamp, None, "UNHEALTHY")

    except Exception as e:
        logging.error(f"Service is DOWN or unreachable: {e}")
        write_csv(timestamp, None, "DOWN")

def write_csv(timestamp, uptime, status):
    file_exists = os.path.isfile(OUTPUT_FILE)

    with open(OUTPUT_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "uptime", "status"])

        writer.writerow([timestamp, uptime, status])

if __name__ == "__main__":
    track_uptime()
