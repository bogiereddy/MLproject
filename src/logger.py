'''
Generates a persistent "black box" audit log to
 track long-running model training.
'''
import logging
import os
import sys
from datetime import datetime
log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs")
os.makedirs(log_path,exist_ok=True)
log_file_path=os.path.join(log_path,log_file)

logging.basicConfig(   # this tells python how to save log files
    
    filename=log_file_path, 
    format="%(asctime)s %(levelname)s %(message)s", 
    level=logging.INFO
)
if __name__=="__main__":
    logging.info("Logging has started.")