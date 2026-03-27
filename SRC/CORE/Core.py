from SRC.UTILS.Logger import Logger
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
        log = Logger()
        response = None

        #? Set service name
        service = service[0].upper()+service[1:]
        serviceName = f"{service}_service"

        #? Try to get Service module
        try:
            module = importlib.import_module(f"SRC.SERVICES.{serviceName}")
            class_ = getattr(module, serviceName)
            response = class_()
        except (ImportError, AttributeError) as e: log.log_error(f"Erro ao importar o modulo: {e}")
        return response
