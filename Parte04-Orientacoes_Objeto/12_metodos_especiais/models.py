class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def __str__(self):
        return f"Olá, meu nome é {self.nome}, tenho {len(self.nome)} anos e minha altura é {float(self):.2f} metros."

    def __le__(self):
        return self.idade

    def __float__(self):
        return self.altura

    def __del__(self):
        print(f"Objeto {self.nome} foi pro saco com sucesso!.🤣👺")