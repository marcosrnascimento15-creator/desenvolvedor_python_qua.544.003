# biblioteca os
import os

# lista vazia
nomes = []

# limpa console
os.system("cls" if os.name == "int" else "clear")

while True:
    nome = input("Informe o nome: ").strip().title()

    # insere ome na lista
    nomes.append(nome)

    print("Deseja inserir mais um nome?")
    print("'s' para sim")
    print("Qualquer outro valor para não")
    opcao = input("Sua resposta: ").strip()
    os.system("cls" if os.name == "int" else "clear")    
    match opcao:
        case "S":
            continue
        case _:
            break
print("Lista de nomes:\n")
for i, nome in enumerate(nomes, start=1):
    print(f"{i}º nome: {nome}")