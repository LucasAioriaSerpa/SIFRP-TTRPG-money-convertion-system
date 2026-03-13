from SRC.UTILS.Logger import Logger
from SRC.CORE.Core import Core
import customtkinter
import traceback
import sys
import os

class Launcher:
    __log = Logger()
    def __init__(self) -> None: self.__log.log_info("Launcher inicializando...")

    def run(self) -> None:
        self.__log.log_info("Inicializando Software...")
        try:
            APP = Core.openService("Main_screen")
            APP.main()
        except Exception as e: 
            self.__log.log_error(f"{e}\n\nTraceback: {traceback.print_exc()}")

if __name__ == "__main__":
    # log = Logger()
    # if getattr(sys, "frozen", False):
    #     try:
    #         DATADIR = os.path.dirname(sys.executable)
    #         customtkinter.__path__ = [os.path.join(DATADIR, 'customtkinter')]
    #     except Exception as e: log.log_error(f"{e}\n\nTrackback: {traceback.print_exc()}")
    Launcher().run()
