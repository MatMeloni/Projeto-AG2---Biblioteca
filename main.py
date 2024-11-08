import tkinter as tk
from Pages.landing_page import LandingPage
from Pages.cadastro_page import CadastroPage
from Pages.categoria_livros_page import CategoriaLivrosPage
from Pages.pagina_inicial import paginainicial
from biblioteca import Biblioteca

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Biblioteca")
        self.geometry("800x600")
        self.frames = {}

        for PageClass in (paginainicial, LandingPage, CadastroPage, CategoriaLivrosPage, Biblioteca):
            page_name = PageClass.__name__
            frame = PageClass(self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PaginaInicial")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
