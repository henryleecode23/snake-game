import logging
import datetime
import traceback

class Logger():
    def __init__(self):
        logging.basicConfig(
                filename=f"./log/{datetime.datetime.now().strftime('%Y-%m-%d-%H.%M.%S.log')}",
                filemode='w', 
                format='%(asctime)s - [%(name)s] %(levelname)s: %(message)s', 
                datefmt='%y-%m-%d %H:%M:%S',
                level=logging.DEBUG)

    @classmethod
    def error(cls, logger_name: str, msg:str =None):
        """
        log the error message to the log file.

        Args:
            logger_name (str): The name of the logger.
            msg (str, optional): The message replace the error info. Defaults to None.
        """
        logger = logging.getLogger(logger_name)
        if msg:
            logger.error("="*10+f"\n{msg}\n"+"="*10)
        else:
            logger.error("="*10+f"\n{traceback.format_exc()}\n"+"="*10)
    
    @classmethod
    def msg(cls, logger_name:str, message:str):
        """
        log message.

        Args:
            logger_name (str): Name of the logger.
            msg (str): Message.
        """
        logger = logging.getLogger(logger_name)
        logger.info(message)
