import psutil
import csv
import os
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [TEMP] %(message)s"
)

OUTPUT_FILE = "system_temperature.csv"
WARNING_THRESHOLD = 75

def read_temperature():
    timestamp = datetime.now().isoformat()

    temps = psutil.sensors_temperatures()

    if not temps:
        logging.warning("No temperature sensors found on this system")
        write_csv(timestamp, None, "NO_SENSOR")
        return
    
    sensor_name = list(temps.keys())[0]
    current_temp = temps[sensor_name][0].current

    if current_temp > WARNING_THRESHOLD:
        logging.warning(f"High temperature detected: {current_temp}°C")
        write_csv(timestamp, current_temp, "HIGH")
    else:
        logging.info(f"Temperature OK: {current_temp}°C")
        write_csv(timestamp, current_temp, "OK")

def write_csv(timestamp, temp, status):
    file_exists = os.path.isfile(OUTPUT_FILE)

    with open(OUTPUT_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "temperature_c", "status"])

        writer.writerow([timestamp, temp, status])

if __name__ == "__main__":
    read_temperature()
