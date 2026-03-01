from SRC.UTILS.Logger import Logger
from SRC.config import APP_PATH
import os
import importlib

class Core:
    """
        Given a service name, return an instance of it
    
        @param service:string Service to be opened
    """

    __log = Logger()
    def __init__(self): self.__log.log_info("Inicializando Core!")
    
    @staticmethod
    def openService(service):
        response = None

        #? Set service name
        service = service[0].upper()+service[1:]
        serviceName = f"{service}_service"

        #? Check if file exists
        if os.path.exists(f"{APP_PATH}/SERVICES/{serviceName}.py"):
            module = importlib.import_module(f"SRC.SERVICES.{serviceName}")
            class_ = getattr(module, serviceName)
            response = class_()

        return response
