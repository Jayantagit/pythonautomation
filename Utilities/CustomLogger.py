import os
import logging


class CustomLogs:
    @staticmethod
    def logger():
         path=os.path.dirname(os.getcwd())+"\\OpenCartFramework\\Logs\\FW.log"
         logger=logging.getLogger(__name__)
         logger.setLevel(logging.INFO)
         file_handler=logging.FileHandler(path)
         logger.addHandler(file_handler)
         return logger