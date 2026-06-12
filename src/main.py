import logging
import yaml
from server import start_server

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Configure logging
logging.basicConfig(
    level=config["app"]["log_level"],
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)

def run():
    logger.info("Starting HTTP server on port 8000")
    start_server(8000)

if __name__ == "__main__":
    run()
