class Pessoa:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

    # O método precisa aceitar um parâmetro extra (ex: nome_pessoa)
    def cumprimentar(self, nome_pessoa):
        return f"Olá {nome_pessoa}, tudo bem? Aqui é a {self.nome}."