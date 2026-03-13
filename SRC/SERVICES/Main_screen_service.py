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
            case "Add":         self._button_add()
            case "Debit":       self._button_debit()

    #? adiciona valor
    def _button_add(self):
        self.__log.log_info("adicionando os baguio :]")

    #? remove valor
    def _button_debit(self):
        self.__log.log_info("debitando os baguio :[")

    """@Override!"""
    def main(self): self.main_screen_view.main()
