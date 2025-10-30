import logging
import os

from from_root import from_root
from datetime import datetime

log_file= f"{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log"

log_dir="log_info"

logs_path=os.path.join(from_root(),log_dir,log_file)

os.makedirs(logs_path,exist_ok=True)

logging.basicConfig(
    filename=logs_path,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)