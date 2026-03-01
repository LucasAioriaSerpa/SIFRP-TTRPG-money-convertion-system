from SRC.UTILS.Logger import Logger
from SRC.CORE.Core import Core

class Main:
    __log = Logger()
    def __init__(self) -> None: self.__log.log_info("Main inicializando...")
    
    def run(self):
        try:
            APP = Core.openService("Main_screen")
            APP.main()
        except Exception as e: self.__log.log_error(str(e))
