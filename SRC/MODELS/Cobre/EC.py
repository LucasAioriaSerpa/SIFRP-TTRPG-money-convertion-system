from SRC.UTILS.Logger import Logger

class EC:
    __Log = Logger()
    def __init__(self, EC_atual, OP):
        self.__Log.log_info("EC inicializando")
        self.EC = EC_atual
        self.OP = OP
    
    def adicao(self):
        pass