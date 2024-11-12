import sqlite3
import tkinter as tk
from tkinter import font as tkFont


#bege_escuro :#e4dfd2
#bege_claro :#eeebe6
#Bg_começo :#eeebe6
#Bg_Final :#888478
#Letra_escuro :#393934
#Letra_claro :#86847c
#Cor botao login: #776333

class pagina_inicial(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg='lightgray')

        #Janela Geral
        root = tk.Tk()
        root.title("Login Page")
        root.geometry("800x600")

        #teste imagem de fundo

        # Carregando a imagem
        imagem_bg = tk.PhotoImage("Pages\Imagens\bg-02.png")

        # Criando um rótulo para exibir a imagem
        label_imagem_bg = tk.Label(root, image=imagem_bg)
        label_imagem_bg.pack()


        # Frame principal de login
        frame = tk.Frame(root, bg='white')
        frame.place(relx=0.5, rely=0.5, anchor='center', width=300, height=450)

        # Titulo
        title_font = tkFont.Font(family="Helvetica", size=24, weight="bold")
        title = tk.Label(self, text="Bem-vindo à Biblioteca Digital!", font=title_font, bg='lightgray', fg='black')
        title.pack(pady=20)

        # Campo de entrada para "Usuário"
        username_label = tk.Label(frame, text="Usuário", bg='white', fg='gray')
        username_label.pack(anchor='w', padx=20)
        self.username_entry = tk.Entry(frame, width=30, borderwidth=2)
        self.username_entry.pack(pady=5, padx=20)

        # Campo de entrada para "Senha"
        password_label = tk.Label(frame, text="Senha", bg='white', fg='gray')
        password_label.pack(anchor='w', padx=20)
        self.password_entry = tk.Entry(frame, width=30, borderwidth=2, show='*')
        self.password_entry.pack(pady=5, padx=20)

        # Botão "Forgot password?"
        forgot_password = tk.Label(frame, text="Forgot password?", bg='white', fg='blue', cursor="hand2")
        forgot_password.pack(anchor='e', padx=20, pady=5)

        #Botão de Login
        login_button = tk.Button(self, text="Login", width=15, height=2, command=self.abrir_livros)
        login_button.pack(pady=10)
       
        #Botão de Cadastro 
        cadastro_button = tk.Button(self, text="Cadastro", width=15, height=2, command=self.realizar_cadastro)
        cadastro_button.pack(pady=10)

        # Texto "Or Sign Up Using"
        social_label = tk.Label(frame, text="Or Sign Up Using", bg='white', fg='gray')
        social_label.pack()

        # Frame para ícones de redes sociais
        social_frame = tk.Frame(frame, bg='white')
        social_frame.pack(pady=10)

    def abrir_livros(self):
        # Mudar para a página de livros
        self.master.show_frame("PaginaLivros")

    def realizar_cadastro(self):
        # Mudar para a página de cadastro (assumindo que ela existe no seu projeto)
        self.master.show_frame("CadastroPage")



class PaginaLivros(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg='white')

        # Título da página
        title = tk.Label(self, text="Livros Disponíveis", font=("Helvetica", 20, "bold"), bg='white')
        title.pack(pady=10)

        # Caixa de texto para exibir os livros
        self.text_box = tk.Text(self, width=80, height=20)
        self.text_box.pack(pady=10)

        # Botão para carregar os livros
        load_button = tk.Button(self, text="Carregar Livros", command=self.carregar_livros)
        load_button.pack(pady=5)

    def carregar_livros(self):
        self.text_box.delete("1.0", tk.END)  # Limpar o conteúdo antes de carregar os livros

        # Conectar ao banco de dados
        conexao = sqlite3.connect('biblioteca.db')
        cursor = conexao.cursor()

        # Consultar os livros
        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()

        # Mostrar os livros na caixa de texto
        for livro in livros:
            self.text_box.insert(tk.END, f"ISBN: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}\n")

        # Fechar a conexão com o banco de dados
        conexao.close()


# Testar a página inicial
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Página Inicial")
    root.geometry("800x600")
    app =pagina_inicial(master=root)
    app.pack()
    root.mainloop()
