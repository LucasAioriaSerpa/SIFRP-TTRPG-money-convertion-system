from SRC.UTILS.Logger import Logger
from SRC.VIEWS.View import View
import customtkinter as ctk

class Main_screen_view(ctk.CTk, View):
    __log = Logger()

    PAD = 10
    COINS = {
        "cobres": {
            "meioVintém(ns)": 0,
            "vintém(ns)": 0,
            "meioTostão(ões)": 0,
            "tostão(ões)": 0,
            "estrela(s)": 0
        },
        "pratas": {
            "gamo(s)": 0,
            "lua(s)": 0
        },
        "ouro": { "dragão(ões)DeOuro(s)": 0 }
    }
    BUTTON_CAPTION = [
        "My button",
        "Exit"
    ]

    def __init__(self, service) -> None:
        self.__log.log_info("main_screen inicializando...")
        super().__init__()
        
        self.title("main_screen")
        self.resizable(width=True, height=True)

        self.main_screen_service = service

        self._make_main_frame()
        self._build()

    def _make_main_frame(self):
        self.mainFrame = ctk.CTkFrame(self, width=200, height=200)
        self.mainFrame.place(x=10, y=10)
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)

    def _build(self):
        self._make_title()
        self._make_options()

    def _make_title(self):
        title = ctk.CTkLabel(
            master=self.mainFrame,
            text="Hello world!",
            font=("Helvetica", 20)
        )
        title.pack(fill="x")

    def _make_options(self):
        frame_buttons = ctk.CTkFrame(self.mainFrame)
        frame_buttons.pack(fill="x", padx=self.PAD, pady=self.PAD)

        for CAPTION in self.BUTTON_CAPTION:
            if CAPTION == "Exit":
                button = ctk.CTkButton(
                    frame_buttons,
                    text=CAPTION,
                    text_color="#FFFFFF",
                    fg_color="#FF2B2B",
                    hover_color="#CE1111",
                    command=self.destroy
                )
            else:
                button = ctk.CTkButton(
                    frame_buttons,
                    text=CAPTION,
                    command=lambda text=CAPTION: self.main_screen_service.button_clicked(text)
                )
            button.pack(fill="x", padx=self.PAD/2, pady=self.PAD)

    """@Override"""
    def main(self): self.mainloop()
    
    """@Override"""
    def close(self): return
