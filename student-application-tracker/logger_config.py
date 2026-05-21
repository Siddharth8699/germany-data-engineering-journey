import logging
import os

# 1. Dynamically locate the absolute path of the project root folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 2. Guarantee the logs directory is created safely internally
os.makedirs(LOG_DIR, exist_ok=True)

# 3. Target the absolute file path for app.log
log_file_path = os.path.join(LOG_DIR, 'app.log')

# 4. Standard basic configuration parameters
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 5. Create the global platform logger instance
logger = logging.getLogger('GlobalTransit')
logger.info("GlobalTransit Platform Logging System Initialized Natively.")