import json
import os
from utils.handler.logging import errorLogger

class ConfigLoader():
    
    @classmethod
    def load(cls, file_path):
        

        if not os.path.exists(os.path.realpath(file_path)):
            return errorLogger.handler("config", f"The file at \"{file_path}\" does not exist.")
        try:
            with open(file_path, "r", encoding="utf8") as f:
                cfg = json.load(f)
            return cfg
        except json.JSONDecodeError as e:
            return errorLogger.handler("config", f"The file at \"{file_path}\" could not be decoded as JSON.\nHere is the error message:\n{e}")
        except Exception as e:
            return errorLogger.handler("config", f"Unknown error durning decode the file at \"{file_path}\" to JSON. \nHere is the error message:\n{e}")
