# importação da biblioteca
import os

# Laço de repetição
while True:
    # limpa tela do terminal
    os.system("cls" if os.name == "nt" else "clear")

    # entrada de dados
    nome = input("Informe seu nome: ").strip().title()
    idade = int(input("Informe sua idade: "))
    cpf = input("informe seu CPF: ").strip()
    email = input("Informe seu email: ").strip().lower()

    os.system("cls" if os.name == "nt" else "clear")

    # saida de dados
    print(f"Nome: {nome}.")
    print(f"Idade: {idade}.")
    print(f"CPF: {cpf}.")
    print(f"E-mail: {email}.")

    # menu
    print("1 - Informar dados de outro usuario")
    print("2 - Sair do Programa")

    opcao = input("Informar a opção desejada: ").strip()

    match opcao:
        case '1':
            continue
        case "2":
            break
        case _:
            print("Opção inválida.")
