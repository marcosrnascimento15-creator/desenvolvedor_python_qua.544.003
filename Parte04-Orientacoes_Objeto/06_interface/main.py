import os
import datetime
from datetime import date
from models import Conta

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def hoje():
    return date.today().strftime("%d/%m/%Y")

def agora():
    return datetime.datetime.now().strftime("%H:%M:%S")

def ler_valor(mensagem):
    """Função utilitária para evitar erros de conversão no input."""
    try:
        return float(input(mensagem).replace(",", "."))
    except ValueError:
        return -1.0

def main():
    cc = Conta(titular="", cpf="", agencia="1234-5", n_conta="10123-4", saldo=0.0)

    limpar()
    cc.titular = input("Informe o nome do titular da conta: ").strip().title()
    cc.cpf = input("Informe o CPF do titular da conta: ").strip()

    limpar()
    print(f"Conta criada no dia {hoje()} às {agora()}.\n")

    while True:
        print("\n--- MENU ---")
        print("0 - Sair do programa")
        print("1 - Consultar dados da conta")
        print("2 - Fazer depósito")
        print("3 - Fazer saque")
        opcao = input("Informe a opção desejada: ").strip()
        
        limpar()
        
        match opcao:
            case "0":
                print("Encerrando o programa. Até logo!")
                break
                
            case "1":
                print(f"Data da consulta: {hoje()} às {agora()}")
                print("-" * 30)
                cc.consultar_conta()
                
            case "2":
                valor = ler_valor("Informe o valor a ser depositado: R$ ")
                if cc.fazer_deposito(valor):
                    print(f"Depósito efetuado com sucesso às {agora()} no dia {hoje()}.")
                    print(f"Saldo atual: R$ {cc.saldo:.2f}")
                else:
                    print("Valor de depósito inválido.")
                    
            case "3":
                valor = ler_valor("Informe o valor do saque: R$ ")
                if cc.fazer_saque(valor):
                    print(f"Saque efetuado com sucesso às {agora()} no dia {hoje()}.")
                    print(f"Saldo atual: R$ {cc.saldo:.2f}")
                else:
                    print("Saque não realizado. Valor inválido ou saldo insuficiente.")
                    
            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    main()