from datetime import date

class Livro:
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor

    def __repr__(self):
        return f"Livro(ISBN={self.isbn}, Título='{self.titulo}', Autor='{self.autor}')"


class Membro:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def idade(self):
        hoje = date.today()
        nascimento = date.fromisoformat(self.data_nascimento)
        return hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

    def __repr__(self):
        return f"Membro(CPF={self.cpf}, Nome='{self.nome}', Data de Nascimento='{self.data_nascimento}')"


class Emprestimo:
    def __init__(self, livro, membro, data_emprestimo, data_devolucao=None):
        self.livro = livro
        self.membro = membro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def esta_atrasado(self):
        if self.data_devolucao:
            return False
        hoje = date.today()
        data_emprestimo = date.fromisoformat(self.data_emprestimo)
        return (hoje - data_emprestimo).days > 14  # Assumindo um período de 14 dias para devolução

    def __repr__(self):
        return (f"Emprestimo(Livro={self.livro.titulo}, Membro={self.membro.nome}, "
                f"Data de Empréstimo='{self.data_emprestimo}', Data de Devolução='{self.data_devolucao}')")
