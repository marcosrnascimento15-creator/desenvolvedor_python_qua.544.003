import os

# Criar uma lista
usuarios = []

# Limpa a tela
os.system("cls" if os.name == "nt" else "clear")

while True:
    # Menu (corrigido o f-string no final)
    print(f"{'-'*20} CRUDicionario {'-'*20}")
    print("1 - Cadastrar novo usuario")
    print("2 - Listar usuarios")
    print("3 - Alterar dados de um usuario")
    print("4 - Deletar usuario")
    print("5 - Sair do programa")
    
    opcao = input("Informe a opção desejada: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    # O match DEVE estar dentro do while
    match opcao:
        case "1":
            # Cria novo dicionario
            usuario = {}
            usuario['nome'] = input("Informe o nome: ").strip().title()
            usuario['cpf'] = input("Informe o CPF: ").strip()
            usuario['email'] = input('Informe seu email: ').strip().lower()

            # Adiciona dicionario na lista
            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")
            print("Usuário cadastrado com sucesso!\n")

        case "2":
            if not usuarios:
                print("Nenhum usuário cadastrado.\n")
            else:
                for usuario in usuarios:
                    for chave, valor in usuario.items():
                        print(f"{chave.capitalize()}: {valor}")
                    print(f"{'-'*40}")
            input("\nPressione ENTER para continuar...")
            os.system("cls" if os.name == "nt" else "clear")

        case "3":
            #TODO: fazer alterar usuario
            pass

        case "4":
            #TODO: Excluir usuario
            pass

        case "5":
            print("Saindo do programa...")
            break

        case _:
            print("Opção inválida!\n")
            continue
    