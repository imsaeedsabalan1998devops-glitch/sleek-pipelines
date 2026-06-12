import logging
import yaml
from health import health_check
from metrics import get_metrics

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
    logger.info("Application started with config")
    logger.info(f"Health: {health_check()}")
    logger.info(f"Metrics: {get_metrics()}")
    return config["app"]["message"]

if __name__ == "__main__":
    output = run()
    print(output)
