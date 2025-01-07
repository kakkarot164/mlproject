import logging
import os
from datetime import datetime

# Log file configuration
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y-%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")  # Correctly separates directory from filename
os.makedirs(logs_dir, exist_ok=True)  # Create only the logs directory

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Example log message
logging.info("Logging setup completed successfully.")


if __name__ =="__main__":
    logging.info("logging has started")