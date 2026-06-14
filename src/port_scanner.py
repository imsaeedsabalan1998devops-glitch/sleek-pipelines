import socket
import csv
import os
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [PORT-SCANNER] %(message)s"
)

TARGET_HOST = "localhost"
TARGET_PORT = 8000
OUTPUT_FILE = "port_scan_history.csv"

def scan_port():
    timestamp = datetime.now().isoformat()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        result = sock.connect_ex((TARGET_HOST, TARGET_PORT))

        if result == 0:
            logging.info(f"Port {TARGET_PORT} is OPEN")
            write_csv(timestamp, "OPEN")
        else:
            logging.warning(f"Port {TARGET_PORT} is CLOSED")
            write_csv(timestamp, "CLOSED")

    except Exception as e:
        logging.error(f"Error scanning port: {e}")
        write_csv(timestamp, "ERROR")

    finally:
        sock.close()

def write_csv(timestamp, status):
    file_exists = os.path.isfile(OUTPUT_FILE)

    with open(OUTPUT_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "status"])

        writer.writerow([timestamp, status])

if __name__ == "__main__":
    scan_port()
