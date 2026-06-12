import logging
import yaml
import os
from server import start_server

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Override config with environment variables
port = int(os.getenv("APP_PORT", 8000))
log_level = os.getenv("APP_LOG_LEVEL", config["app"]["log_level"])

# Configure logging
logging.basicConfig(
    level=log_level,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)

def run():
    logger.info(f"Starting HTTP server on port {port}")
    start_server(port)

if __name__ == "__main__":
    run()
