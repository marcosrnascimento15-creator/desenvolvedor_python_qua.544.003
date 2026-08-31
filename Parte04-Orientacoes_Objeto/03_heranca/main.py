import os

from models import PessoaFisica, PessoaJuridica

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = PessoaFisica(nome="", cpf="",email="", telefone="", endereco="" )
    empresa = PessoaJuridica(razao_social="", nome_fantasia="",cnpj="",email="",telefone="",endereco="")

    limpar()

    # Informa os valores do usuario
    usuario.nome = input("Informe o nome de usuario: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.email = input("Informe o e-mail do usuario: ").strip().lower()
    usuario.telefone = input("Informe o telefone do usuario: ").strip()
    usuario.endereco = input("Informe o endereço do usuario: ")

    limpar()

    # Informa os valores da empresa
    empresa.razao_social = input("Informe nome juridico da empresa: ").strip()
    empresa.nome_fantasia = input("Informe o nome da Empresa: ").strip()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.email = input("Informe o E-mail da empresa: ").strip().lower()
    empresa.telefone = input("Informe o Telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço da empresa: ")

    limpar()

    # saida de dados

    usuario.exibir_dados()
    empresa.exibir_dados()
 

if __name__ == "__main__":
    main()