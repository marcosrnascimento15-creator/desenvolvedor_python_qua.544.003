nomes = [
    "Fulano",
    "Cicrano",
    "Beltrano",
    "João",
    "Maria",
    "José",
    "Esmeralda",
    "Juventina"
]

# usuario informa o nome que dseja alterar
nome_antigo = input("Informe o nome que deseja alterar: ").strip().title()

# armazenaa posição do nome da lista caso exista
if nome_antigo in nomes:
    indice = nomes.index(nome_antigo)
    nomes[indice] = input("Informe novo nome: ").strip().title()
    print("Nome alterado com sucesso!")
    for nome in nomes:
        print(nome)
else:
    print("Nome não encontrado.")