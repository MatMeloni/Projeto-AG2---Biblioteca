import tkinter as tk
from tkinter import font as tkFont
from PIL import Image, ImageTk, ImageFilter  # Biblioteca Pillow para carregar imagens

def show_frame(frame):
    frame.tkraise()
# Criação da janela principal
root = tk.Tk()
root.title("Login Page")
root.geometry("800x600")

# Carregar a imagem de fundo
background_image = Image.open(r"Pages/Imagens/bg-01.jpg")
background_image = background_image.filter(ImageFilter.GaussianBlur(55))  # Substitua pelo caminho da sua imagem
background_image = background_image.resize((800, 600), Image.Resampling.LANCZOS)  # Ajuste o tamanho da imagem
background_photo = ImageTk.PhotoImage(background_image)

# Colocar a imagem de fundo na janela
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Frame principal de login
login_frame = tk.Frame(root, bg='white')
login_frame.place(relx=0.5, rely=0.5, anchor='center', width=300, height=450)

# Título "Login"
title_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
title = tk.Label(login_frame, text="Login", font=title_font, bg='white', fg='black')
title.pack(pady=20)

# Campo de entrada para "Username"
username_label = tk.Label(login_frame, text="Username", bg='white', fg='gray')
username_label.pack(anchor='w', padx=20)
username_entry = tk.Entry(login_frame, width=30, borderwidth=2)
username_entry.pack(pady=5, padx=20)

# Campo de entrada para "Password"
password_label = tk.Label(login_frame, text="Password", bg='white', fg='gray')
password_label.pack(anchor='w', padx=20)
password_entry = tk.Entry(login_frame, width=30, borderwidth=2, show='*')
password_entry.pack(pady=5, padx=20)

# Botão "Forgot password?"
forgot_password = tk.Label(login_frame, text="Forgot password?", bg='white', fg='blue', cursor="hand2")
forgot_password.pack(anchor='e', padx=20, pady=5)

# Função de callback do botão de login
def verificar_login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Lógica simples de verificação de login (pode ser substituída por validação real)
    if username == "admin" and password == "1234":
        show_frame(livros_frame)  # Redireciona para o frame de livros
    else:
        tk.messagebox.showerror("Erro", "Credenciais inválidas. Tente novamente.")

# Botão de "Login"
login_button = tk.Button(login_frame, text="LOGIN", width=20, height=2, bg='#8f44fd', fg='white', borderwidth=0, command=verificar_login)
login_button.pack(pady=20)

# Texto "Or Sign Up Using"
social_label = tk.Label(login_frame, text="Or Sign Up Using", bg='white', fg='gray')
social_label.pack()
# Frame para ícones de redes sociais
social_frame = tk.Frame(login_frame, bg='white')
social_frame.pack(pady=10)

# Carregar ícones
facebook_icon = ImageTk.PhotoImage(Image.open(r"Pages\Imagens\facebook.png").resize((30, 30), Image.Resampling.LANCZOS))
instagram_icon = ImageTk.PhotoImage(Image.open(r"Pages\Imagens\instagram.jpeg").resize((30, 30), Image.Resampling.LANCZOS))
twitter_icon = ImageTk.PhotoImage(Image.open(r"Pages\Imagens\Twitter.png").resize((30, 30), Image.Resampling.LANCZOS))

# Botões com ícones
fb_button = tk.Button(social_frame, image=facebook_icon, borderwidth=0, bg='white', cursor="hand2")
fb_button.grid(row=0, column=0, padx=5)
insta_button = tk.Button(social_frame, image=instagram_icon, borderwidth=0, bg='white', cursor="hand2")
insta_button.grid(row=0, column=1, padx=5)
twitter_button = tk.Button(social_frame, image=twitter_icon, borderwidth=0, bg='white', cursor="hand2")
twitter_button.grid(row=0, column=2, padx=5)

# Inicializar a página de login primeiro
show_frame(login_frame)

root.mainloop()

