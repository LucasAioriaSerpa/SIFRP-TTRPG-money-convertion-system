from SRC.UTILS.Logger import Logger
from SRC.Main import Main

class Launcher:
    __log = Logger()
    __main = Main()
    def __init__(self) -> None: self.__log.log_info("Launcher inicializando...")

    def run(self) -> None:
        self.__log.log_info("Inicializando Software...")
        self.__main.run()

if __name__ == "__main__": Launcher().run()
