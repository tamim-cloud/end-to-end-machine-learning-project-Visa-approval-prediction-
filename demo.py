import sys
from us_visa.logger import logging
from us_visa.exception import CustomException

#logging.info("demo from demo.py file")

try:
    r=5/0
    print(r)
except Exception as e:
    logging.info("Exception occured in demo.py file")
    raise CustomException(e, sys)