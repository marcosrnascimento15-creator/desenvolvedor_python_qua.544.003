from import Pessoa, Conta
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    # Instanciando a Pessoa 
    nome = input("Informe o nome do titular: ").strip().title()
    cpf = input("Informe o CPF: ").strip()
    titular = Pessoa(nome=nome, cpf=cpf)

    # Instanciando a Conta com a Associação da Pessoa
    agencia = input("Informe a agência: ").strip()
    n_conta = input("Informe o número da conta: ").strip()
    saldo_inicial = float(
        input("Informe o saldo inicial: ").replace(",", ".")
    )

    conta = Conta(
        titular=titular,
        agencia=agencia,
        n_conta=n_conta,
        saldo=saldo_inicial,
    )

    print("\n" + "=" * 30)
    # Executando os métodos da classe
    conta.consultar_dados()
    print("\n")