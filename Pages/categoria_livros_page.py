import tkinter as tk

class CategoriaLivrosPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=0, sticky="nsew")
        self.criar_widgets()

    def criar_widgets(self):
        self.label_titulo = tk.Label(self, text="Categorias de Livros", font=("Montserrat", 24, "bold"))
        self.label_titulo.grid(row=0, column=0, pady=20)

        self.button_voltar = tk.Button(self, text="Voltar", command=lambda: self.master.show_frame("PaginaInicial"))
        self.button_voltar.grid(row=1, column=0, pady=10)
