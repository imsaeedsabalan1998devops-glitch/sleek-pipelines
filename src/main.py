import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)

def run():
    logger.info("Application started")
    return "DevOps Playground is alive 🔥"

if __name__ == "__main__":
    output = run()
    print(output)
