from SRC.UTILS.Logger import Logger
import abc

class View(metaclass=abc.ABCMeta):
    __log = Logger()
    def __init__(self): self.__log.log_info("View inicializando...")

    @abc.abstractmethod
    def main(self): return
    
    @abc.abstractmethod
    def close(self): return
