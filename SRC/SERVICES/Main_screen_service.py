from SRC.UTILS.Logger import Logger
from SRC.CORE.Service import Service
from SRC.CORE.Core import Core

class Main_screen_service(Service):
    __log = Logger()
    def __init__(self):
        self.__log.log_info("Inicializando Main_screen_service!")
        self.main_screen_view = self.loadView("main_screen")

    def __debug_print_input_coins(self):
        for key, item in self.main_screen_view.INPUT_COINS.items():
            self.__log.log_info(f"chave: {key}")
            self.__log.log_info(f"  item: {item}")
            for i, y in item.items():
                self.__log.log_info(f"      chave: {i}")
                self.__log.log_info(f"          item: {y}")
                self.__log.log_info(f"          conteudo: {y.get("0.0", "end-1c")}")

    def button_clicked(self, caption):
        """when a btn is clicked"""
        """
        * change screen
        ? core = Core.openService("fileNameClassService")
        ? core.main()
        """
        self.__debug_print_input_coins()
        match caption:
            case "Add":         self._button_add()
            case "Debit":       self._button_debit()

    #? adiciona valor
    def _button_add(self):
        self.__log.log_info("adicionando os baguio :]")
        for type_coin, coins in self.main_screen_view.INPUT_COINS.items():
            for sub_type_coin, coin_input in coins.items():
                self.__log.log_info(f"{type_coin} de {sub_type_coin} com: {coin_input.get("0.0", "end-1c")}")
                coin_input.delete("0.0", "end")

    #? remove valor
    def _button_debit(self):
        self.__log.log_info("debitando os baguio :[")

    """@Override!"""
    def main(self): self.main_screen_view.main()
