# classe Pessoa
class Pessoa:
    # método construtor
    def __init__(self, nome, idade, email, altura):
        # Atributos
        self.nome = nome
        self.idade = idade
        self.email = email
        self.altura = altura

    # metodo
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"idade: {self.idade} anos")
        print(f"email: {self.email}")
        print(f"altura: {self.altura} metros")

def main():
    # instancia a classe (cria o objeto)
    usuario = Pessoa(nome="", idade="", email="", altura=0.0)

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int(input("Informe a idade: "))
    usuario.email = input("Informe email: ").strip().lower()
    usuario.altura = float(input("Informe a altura em metros: ").replace(",","."))

    usuario.exibir_dados()



if __name__ == "__main__":
    main()
        