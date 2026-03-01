from SRC.UTILS.Logger import Logger
from SRC.CORE.Service import Service
from SRC.CORE.Core import Core

class Main_screen_service(Service):
    __log = Logger()
    def __init__(self):
        self.__log.log_info("Inicializando Main_screen_service!")
        self.main_screen_view = self.loadView("main_screen")
    
    def button_clicked(self, caption):
        """when a btn is clicked"""
        """
        * change screen
        ? core = Core.openService("fileNameClassService")
        ? core.main()
        """
        
        match caption:
            case "My button":
                self.__log.log_info("Hello world!")
        ...

    """@Override!"""
    def main(self): self.main_screen_view.main()
