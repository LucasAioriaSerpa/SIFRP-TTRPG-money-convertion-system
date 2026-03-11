from SRC.UTILS.Logger import Logger
from SRC.CORE.Core import Core

class Launcher:
    __log = Logger()
    def __init__(self) -> None: self.__log.log_info("Launcher inicializando...")

    def run(self) -> None:
        self.__log.log_info("Inicializando Software...")
        try:
            APP = Core.openService("Main_screen")
            APP.main()
        except Exception as e: self.__log.log_error(str(e))

if __name__ == "__main__": Launcher().run()
