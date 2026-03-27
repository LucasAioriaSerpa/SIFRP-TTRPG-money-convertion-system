from SRC.UTILS.Logger import Logger
import importlib
import abc

class Service(metaclass=abc.ABCMeta):
    __log = Logger()
    def __init__(self): self.__log.log_info("Inicializando Service!")
    
    """
        Executes service and associated view with it.
    """
    @abc.abstractmethod
    def main(self): return
    
    """
        Given a view name, return an instance of it
    
        @param viewName:string View to be opened
    """
    def loadView(self, viewName):
        log = Logger()
        response = None
        
        #? Set view name
        viewName = viewName[0].upper()+viewName[1:]+"_view"
        
        #? Try to get View module
        try:
            module = importlib.import_module("SRC.VIEWS."+viewName)
            class_ = getattr(module, viewName)
            response = class_(self)
        except (ImportError, AttributeError) as e: log.log_error(f"Erro ao importar o modulo: {e}")

        return response
