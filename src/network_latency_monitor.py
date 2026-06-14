import subprocess
import csv
import os
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [NET-LATENCY] %(message)s"
)

TARGET = "8.8.8.8"  # Google DNS
OUTPUT_FILE = "network_latency.csv"

def ping_target():
    timestamp = datetime.now().isoformat()

    try:
        result = subprocess.run(
            ["ping", "-c", "1", TARGET],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            latency = parse_latency(result.stdout)
            logging.info(f"Network OK. Latency: {latency} ms")
            write_csv(timestamp, latency, "UP")
        else:
            logging.warning("Network unreachable")
            write_csv(timestamp, None, "DOWN")

    except Exception as e:
        logging.error(f"Error running ping: {e}")
        write_csv(timestamp, None, "ERROR")

def parse_latency(output):
    for line in output.split("\n"):
        if "time=" in line:
            return float(line.split("time=")[1].split(" ")[0])
    return None

def write_csv(timestamp, latency, status):
    file_exists = os.path.isfile(OUTPUT_FILE)

    with open(OUTPUT_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "latency_ms", "status"])

        writer.writerow([timestamp, latency, status])

if __name__ == "__main__":
    ping_target()
