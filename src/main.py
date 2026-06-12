import logging
import yaml
from health import health_check

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
    return config["app"]["message"]

if __name__ == "__main__":
    logger.info(f"Health: {health_check()}")
    output = run()
    print(output)
