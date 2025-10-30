import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE= f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

log_dir="log_info"

logs_folder=os.path.join(from_root(),log_dir)
os.makedirs(logs_folder,exist_ok=True)

logs_path=os.path.join(logs_folder,LOG_FILE)
logging.basicConfig(
    filename=logs_path,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)