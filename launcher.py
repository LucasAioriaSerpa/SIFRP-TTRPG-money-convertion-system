
from SRC.UTILS.Logger import Logger

class Launcher:
    __log = Logger(True)
    def __init__(self) -> None: self.__log.log_info("Launcher inicializando...")

    def run(self) -> None:
        self.__log.log_info("Inicializando Software...")
        self.__log.log_info("Abrindo primeira interface gráfica...")


if __name__ == "__main__": Launcher().run()
