import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [HEALTH-CHECK] %(message)s"
)

HEALTH_URL = "http://localhost:8000/health"

def check_service_health():
    try:
        response = requests.get(HEALTH_URL, timeout=3)
        if response.status_code == 200:
            logging.info("Service is UP and healthy.")
        else:
            logging.warning(f"Service responded but not healthy: {response.status_code}")
    except Exception as e:
        logging.error(f"Service is DOWN or unreachable: {e}")

if __name__ == "__main__":
    check_service_health()
