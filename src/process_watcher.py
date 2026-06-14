import psutil
import csv
import os
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [PROCESS-WATCHER] %(message)s"
)

TARGET_PROCESS_NAME = "python"
OUTPUT_FILE = "process_watch.csv"

def check_process():
    timestamp = datetime.now().isoformat()
    running = False

    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if TARGET_PROCESS_NAME in proc.info['name'] or \
               any(TARGET_PROCESS_NAME in cmd for cmd in proc.info['cmdline']):
                running = True
                break
        except Exception:
            continue

    if running:
        logging.info(f"Process '{TARGET_PROCESS_NAME}' is RUNNING")
        write_csv(timestamp, "RUNNING")
    else:
        logging.warning(f"Process '{TARGET_PROCESS_NAME}' is NOT running")
        write_csv(timestamp, "NOT_RUNNING")

def write_csv(timestamp, status):
    file_exists = os.path.isfile(OUTPUT_FILE)

    with open(OUTPUT_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "status"])

        writer.writerow([timestamp, status])

if __name__ == "__main__":
    check_process()
