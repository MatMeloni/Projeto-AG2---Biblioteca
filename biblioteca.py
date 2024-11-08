import sqlite3
from modelos import Livro, Membro, Emprestimo
from datetime import date

class Biblioteca:
    def __init__(self, db_name='biblioteca.db'):
        self.conexao = sqlite3.connect(db_name)
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        # Criação das tabelas se não existirem
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            isbn TEXT PRIMARY KEY,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS membros (
            cpf TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            data_nascimento TEXT NOT NULL
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS emprestimos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT,
            cpf TEXT,
            data_emprestimo TEXT,
            data_devolucao TEXT,
            FOREIGN KEY (isbn) REFERENCES livros (isbn),
            FOREIGN KEY (cpf) REFERENCES membros (cpf)
        )
        ''')
        self.conexao.commit()

    def incluir_livro(self, livro):
        try:
            self.cursor.execute('INSERT INTO livros (isbn, titulo, autor) VALUES (?, ?, ?)', 
                                (livro.isbn, livro.titulo, livro.autor))
            self.conexao.commit()
            print("Livro incluído com sucesso.")
        except sqlite3.IntegrityError as e:
            print(f"Erro ao incluir livro: {e}")

    def incluir_membro(self, membro):
        try:
            self.cursor.execute('INSERT INTO membros (cpf, nome, data_nascimento) VALUES (?, ?, ?)', 
                                (membro.cpf, membro.nome, membro.data_nascimento))
            self.conexao.commit()
            print("Membro incluído com sucesso.")
        except sqlite3.IntegrityError as e:
            print(f"Erro ao incluir membro: {e}")

    def registrar_emprestimo(self, emprestimo):
        try:
            self.cursor.execute('INSERT INTO emprestimos (isbn, cpf, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)', 
                                (emprestimo.livro.isbn, emprestimo.membro.cpf, emprestimo.data_emprestimo, emprestimo.data_devolucao))
            self.conexao.commit()
            print("Empréstimo registrado com sucesso.")
        except sqlite3.IntegrityError as e:
            print(f"Erro ao registrar empréstimo: {e}")

    def devolver_livro(self, isbn, cpf):
        self.cursor.execute('UPDATE emprestimos SET data_devolucao = ? WHERE isbn = ? AND cpf = ? AND data_devolucao IS NULL', 
                            (date.today().strftime('%Y-%m-%d'), isbn, cpf))
        self.conexao.commit()
        print("Livro devolvido com sucesso.")

    def get_livros_disponiveis(self):
        self.cursor.execute('SELECT * FROM livros WHERE isbn NOT IN (SELECT isbn FROM emprestimos WHERE data_devolucao IS NULL)')
        livros = self.cursor.fetchall()
        return [Livro(isbn, titulo, autor) for isbn, titulo, autor in livros]

    def get_livros_emprestados(self):
        self.cursor.execute('SELECT * FROM emprestimos WHERE data_devolucao IS NULL')
        emprestimos = self.cursor.fetchall()
        resultados = []
        for id_, isbn, cpf, data_emprestimo, data_devolucao in emprestimos:
            self.cursor.execute('SELECT * FROM livros WHERE isbn = ?', (isbn,))
            livro = self.cursor.fetchone()
            self.cursor.execute('SELECT * FROM membros WHERE cpf = ?', (cpf,))
            membro = self.cursor.fetchone()
            if livro and membro:
                livro_obj = Livro(livro[0], livro[1], livro[2])
                membro_obj = Membro(membro[0], membro[1], membro[2])
                emprestimo_obj = Emprestimo(livro_obj, membro_obj, data_emprestimo, data_devolucao)
                resultados.append(emprestimo_obj)
        return resultados

    def fechar_conexao(self):
        self.conexao.close()
