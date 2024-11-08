import tkinter as tk

class CadastroPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=0, sticky="nsew")
        self.create_widgets()

    def create_widgets(self):
        # Adicione os widgets de cadastro aqui
        pass
