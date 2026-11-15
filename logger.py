# Mock Logging Module

import logging

logging.basicConfig(level=logging.INFO)

def log_message(message):
    logging.info(message)




if __name__ == "__main__":
    log_message("Application started successfully")
