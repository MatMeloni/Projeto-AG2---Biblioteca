import tkinter as tk
from tkinter import font as tkFont
from PIL import Image, ImageTk, ImageFilter # Biblioteca Pillow para carregar imagens

class paginainicial(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=0, sticky="nsew")
    
    #bege_escuro :#e4dfd2
    #bege_claro :#eeebe6
    #Bg_começo :#eeebe6
    #Bg_Final :#888478
    #Letra_escuro :#393934
    #Letra_claro :#86847c
    #Cor botao login: #776333

def show_frame(frame):
    frame.tkraise()
          
    # Criação da janela principal
    root = tk.Tk()
    root.title("Login Page")
    root.geometry("800x600")

    # Carregar a imagem de fundo
    background_image = Image.open(r"Pages\Imagens\bg-02.png")
    background_image = background_image.filter(ImageFilter.GaussianBlur(55))  # Substitua pelo caminho da sua imagem
    background_image = background_image.resize((800, 600), Image.Resampling.LANCZOS)  # Ajuste o tamanho da imagem
    background_photo = ImageTk.PhotoImage(background_image)

    # Colocar a imagem de fundo na janela
    background_label = tk.Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    # Frame principal de login
    frame = tk.Frame(root, bg='white')
    frame.place(relx=0.5, rely=0.5, anchor='center', width=300, height=450)

    # Título "Login"
    title_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
    title = tk.Label(frame, text="Login", font=title_font, bg='white', fg='#393934')
    title.pack(pady=20)

    # Campo de entrada para "Usuário"
    username_label = tk.Label(frame, text="Usuário", bg='white', fg='gray')
    username_label.pack(anchor='w', padx=20)
    username_entry = tk.Entry(frame, width=30, borderwidth=2)
    username_entry.pack(pady=5, padx=20)

    # Campo de entrada para "Senha"
    password_label = tk.Label(frame, text="Senha", bg='white', fg='gray')
    password_label.pack(anchor='w', padx=20)
    password_entry = tk.Entry(frame, width=30, borderwidth=2, show='*')
    password_entry.pack(pady=5, padx=20)

    # Botão "Forgot password?"
    forgot_password = tk.Label(frame, text="Forgot password?", bg='white', fg='blue', cursor="hand2")
    forgot_password.pack(anchor='e', padx=20, pady=5)

    # Botão de "Login"
    login_frame = tk.Frame(root, bg='white')
    login_frame.grid(row=0, column=0, sticky='nsew')
    login_button = tk.Button(frame, text="LOGIN", width=20, height=2, bg='#776333', fg='white', borderwidth=0)
    login_button.pack(pady=20)

    # Botão "SIGN UP" no frame de login para redirecionar para o frame de cadastro
    signup_frame = tk.Frame(root, bg='white')
    signup_frame.grid(row=0, column=0, sticky='nsew')
    signup_button = tk.Button(frame, text="SIGN UP", bg='white', fg='blue', cursor="hand2", borderwidth=0, command=lambda: show_frame(signup_frame))
    signup_button.pack()

    # Texto "Or Sign Up Using"
    social_label = tk.Label(frame, text="Or Sign Up Using", bg='white', fg='gray')
    social_label.pack()

    # Frame para ícones de redes sociais
    social_frame = tk.Frame(frame, bg='white')
    social_frame.pack(pady=10)

    # Carregar ícones 
    facebook_icon = ImageTk.PhotoImage(Image.open(r"Pages\Imagens\Logo_Facebook.png").resize((30, 30), Image.Resampling.LANCZOS))
    instagram_icon = ImageTk.PhotoImage(Image.open(r"Pages\Imagens\Logo_Instagram.png").resize((30, 30), Image.Resampling.LANCZOS))
    twitter_icon = ImageTk.PhotoImage(Image.open(r"Pages\Imagens\Logo_Twitter.png").resize((30, 30), Image.Resampling.LANCZOS))

    # Botões com ícones
    fb_button = tk.Button(social_frame, image=facebook_icon, borderwidth=0, bg='white', cursor="hand2")
    fb_button.grid(row=0, column=0, padx=5)
    insta_button = tk.Button(social_frame, image=instagram_icon, borderwidth=0, bg='white', cursor="hand2")
    insta_button.grid(row=0, column=1, padx=5)
    twitter_button = tk.Button(social_frame, image=twitter_icon, borderwidth=0, bg='white', cursor="hand2")
    twitter_button.grid(row=0, column=2, padx=5)
    
def run(self):
    self.janela.mainloop()
