import tkinter as tk
import Pages.pagina_inicial

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Biblioteca")
        self.geometry("800x600")
        self.frames = {}

        for PageClass in (Pages.pagina_inicial):
            page_name = PageClass.__name__
            frame = PageClass(self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("paginainicial")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
