import hashlib
import os
import csv
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [FILE-INTEGRITY] %(message)s"
)

TARGET_DIR = "src"
OUTPUT_FILE = "file_integrity.csv"

def hash_file(path):
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            sha.update(chunk)
    return sha.hexdigest()

def scan_files():
    timestamp = datetime.now().isoformat()
    results = []

    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            file_hash = hash_file(full_path)
            results.append((full_path, file_hash))

    write_csv(timestamp, results)
    logging.info(f"Scanned {len(results)} files")

def write_csv(timestamp, results):
    file_exists = os.path.isfile(OUTPUT_FILE)

    with open(OUTPUT_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "file_path", "sha256"])

        for path, sha in results:
            writer.writerow([timestamp, path, sha])

if __name__ == "__main__":
    scan_files()
