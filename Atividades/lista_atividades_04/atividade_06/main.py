from models import Pessoa, Conta
import os

def limpar_tela():
    # Limpa a tela do terminal
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

    limpar_tela()

    # Testando 
    val_deposito = float(
        input("Digite o valor para depósito: ").replace(",", ".")
    )
    conta.depositar(val_deposito)

    val_saque = float(input("Digite o valor para saque: ").replace(",", "."))
    conta.sacar(val_saque)

    limpar_tela()
        
    print("\n")
    conta.gerar_extrato()


if __name__ == "__main__":
    main()