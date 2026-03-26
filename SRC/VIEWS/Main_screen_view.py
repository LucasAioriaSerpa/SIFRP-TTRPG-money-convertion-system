from SRC.UTILS.Logger import Logger
from SRC.VIEWS.View import View

import customtkinter as ctk

class Main_screen_view(ctk.CTk, View):
    __log = Logger()

    PAD = 20
    SIZE_INPUT_COINS = ({"x": 40, "y": 10})
    COIN_TYPES = [
        "cobres",
        "pratas",
        "ouro"
    ]
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
        "Add",
        "Debit",
        "History",
        "Save Wallet",
        "Load Wallet",
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
        self.mainFrame = ctk.CTkFrame(self)
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD, fill="both", expand=True)

        self.mainFrame.grid_columnconfigure(0, weight=1)

    def _build(self):
        self._make_title()
        self._make_coins()
        self._make_options()

    def _make_title(self):
        title = ctk.CTkLabel(
            master=self.mainFrame,
            text="Convertor de moedas do sistema SIFRP-TTRPG!",
            font=("Helvetica", 20)
        )
        title.grid(row=0, column=0, sticky="nsew")

    def _make_coins(self):
        frame_coins = ctk.CTkFrame(self.mainFrame)
        frame_coins.grid(row=1, column=0, padx=self.PAD, pady=self.PAD)

        self.__make_player_coins(frame_coins)
        self.__make_player_coins_input(frame_coins)

    def __make_player_coins(self, main_frame: ctk.CTkFrame):
        frame_player_coins = self.___make_frame_with_title(
            title="Moedas Atuais!",
            font=("Helvetica", 20),
            main_frame=main_frame,
            row=0, column=0
        )
        
        self.___make_labels_inputs_coins(frame_player_coins, True)

    def __make_player_coins_input(self, main_frame: ctk.CTkFrame):
        frame_player_coins_input = self.___make_frame_with_title(
            title="Inserção de moeda",
            font=("Helvetica", 20),
            main_frame=main_frame,
            row=0, column=1
        )

        self.___make_labels_inputs_coins(frame_player_coins_input, False)

    def ___make_frame_with_title(self, title: str, font: tuple[str, int], main_frame: ctk.CTkFrame, row: int, column: int) -> ctk.CTkFrame:
        frame = ctk.CTkFrame(main_frame)
        frame.grid(
            row=row,
            column=column,
            padx=self.PAD, pady=self.PAD,
            sticky="nsew"
        )

        title_label = ctk.CTkLabel(master=frame, text=title, font=font)
        title_label.grid(row=0, column=0, sticky="nsew")

        return frame

    def ___make_labels_inputs_coins(self, frame: ctk.CTkFrame, activate_labels: bool):
        ROW_COIN_TYPE = 2
        for i in range(len(self.COINS)):
            COIN_TYPE = self.COIN_TYPES[i]
            COIN_SUB_TYPE_OBJ = list(self.COINS.values())[i]
            
            type_text = ctk.CTkLabel(frame, text=COIN_TYPE.upper())
            type_text.grid(row=ROW_COIN_TYPE, column=0)
            
            ROW_COIN_TYPE = ROW_COIN_TYPE + 1
            
            frame_sub_coins = ctk.CTkFrame(frame)
            frame_sub_coins.grid(row=ROW_COIN_TYPE, column=0, padx=self.PAD, sticky="nsew")
            
            for y in range(len(COIN_SUB_TYPE_OBJ)):
                COIN_SUB_TYPE = list(COIN_SUB_TYPE_OBJ.keys())[y]
                COIN_VALUE = list(COIN_SUB_TYPE_OBJ.values())[y]
                ROW_SUB_COIN_TYPE = ROW_COIN_TYPE + y + 1
                
                subType_text = ctk.CTkLabel(frame_sub_coins, text=f"{COIN_SUB_TYPE}: ")
                subType_text.grid(row=ROW_SUB_COIN_TYPE, column=0, padx=self.PAD, sticky="nsew")
                
                if activate_labels:
                    value = ctk.CTkLabel(frame_sub_coins, text=COIN_VALUE)
                    value.grid(row=ROW_SUB_COIN_TYPE, column=1, padx=self.PAD, sticky="nsew")
                    continue
                
                input_ = ctk.CTkTextbox(
                    frame_sub_coins,
                    activate_scrollbars=False,
                    width=self.SIZE_INPUT_COINS["x"], height=self.SIZE_INPUT_COINS["y"]
                )
                input_.grid(row=ROW_SUB_COIN_TYPE, column=1, padx=self.PAD, sticky="nsew")

            ROW_COIN_TYPE = ROW_SUB_COIN_TYPE + 1

    def _make_options(self):
        frame_buttons = ctk.CTkFrame(self.mainFrame)
        frame_buttons.grid(row=2, column=0, padx=self.PAD, pady=self.PAD, sticky="nsew")

        for CAPTION in self.BUTTON_CAPTION:
            match CAPTION:
                case "Exit":
                    button = ctk.CTkButton(
                        frame_buttons,
                        text=CAPTION,
                        text_color="#F2F2F2",
                        fg_color="#EE1515",
                        hover_color="#B60909",
                        command=self.destroy
                    )
                case _:
                    button = ctk.CTkButton(
                        frame_buttons,
                        text=CAPTION,
                        command=lambda text=CAPTION: self.main_screen_service.button_clicked(text)
                    )
            button.pack(side="left", fill="both", padx=self.PAD/2, pady=self.PAD, expand=True)

    """@Override"""
    def main(self): self.mainloop()
    
    """@Override"""
    def close(self): return
