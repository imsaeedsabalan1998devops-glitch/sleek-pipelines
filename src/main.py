import logging
import yaml

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
    output = run()
    print(output)
