import os

from models import PessoaFisica, PessoaJuridica

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():

    usuario = PessoaFisica(nome="",cpf="",email="",telefone="")
    empresa = PessoaJuridica(nome_fantasia="",cnpj="",email="",telefone="")

    limpar()

    usuario.nome = input("Informe o nome do usuario: ").strip().title()
    usuario.cpf = input("Informe o CPF do usuario: ").strip()
    usuario.email = input("Informe o e-mail do usuario: ").strip().lower()
    usuario.telefone = input("Informe o telefone do usuario: ").strip()

    limpar()

    empresa.nome_fantasia = input("Informe o Nome da Empresa: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ: ")
    empresa.email = input("Informe o E-mail da empresa: ").strip().lower()
    empresa.telefone = input("Informe o telefone da Empresa: ").strip()

    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"E-mail: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")
    print(f"Nome da Empresa: {empresa.nome_fantasia}")
    print(f"CNPJ da empresa: {empresa.cnpj}")
    print(f"E-mail da empresa: {empresa.email}")
    print(f"Telefone da Empresa: {empresa.telefone}")

if __name__ == "__main__":
    main()
