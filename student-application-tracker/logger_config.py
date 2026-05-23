import logging
import os


# Project root = folder where logger_config.py exists
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

# Create logs folder inside project
LOG_DIR = os.path.join(
    BASE_DIR,
    "logs"
)

os.makedirs(
    LOG_DIR,
    exist_ok=True
)

# Final log file
log_file_path = os.path.join(
    LOG_DIR,
    "app.log"
)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global logger
logger = logging.getLogger(
    "GermanyPreparation"
)

logger.info(
    "Germany Preparation Logging System Initialized."
)