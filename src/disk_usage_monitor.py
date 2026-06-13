import shutil
import csv
import os
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [DISK] %(message)s"
)

OUTPUT_FILE = "disk_usage.csv"
WARNING_THRESHOLD = 85  # درصد هشدار

def monitor_disk():
    timestamp = datetime.now().isoformat()

    total, used, free = shutil.disk_usage("/")
    percent_used = round((used / total) * 100, 2)

    if percent_used > WARNING_THRESHOLD:
        logging.warning(f"Disk usage HIGH: {percent_used}%")
    else:
        logging.info(f"Disk usage OK: {percent_used}%")

    write_csv(timestamp, percent_used)

def write_csv(timestamp, percent_used):
    file_exists = os.path.isfile(OUTPUT_FILE)

    with open(OUTPUT_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "disk_percent_used"])

        writer.writerow([timestamp, percent_used])

if __name__ == "__main__":
    monitor_disk()
