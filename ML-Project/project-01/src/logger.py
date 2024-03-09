import logging
import os
from datetime import datetime

LOG_FILE = f"{datatime.now().strftime('%m-%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE)

def get_logger(name):
