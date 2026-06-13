import psutil
import csv
import os
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [RESOURCE] %(message)s"
)

OUTPUT_FILE = "resource_usage.csv"

def monitor_resources():
    timestamp = datetime.now().isoformat()

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    logging.info(f"CPU: {cpu}% | RAM: {ram}%")

    write_csv(timestamp, cpu, ram)

def write_csv(timestamp, cpu, ram):
    file_exists = os.path.isfile(OUTPUT_FILE)

    with open(OUTPUT_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "cpu_percent", "ram_percent"])

        writer.writerow([timestamp, cpu, ram])

if __name__ == "__main__":
    monitor_resources()
