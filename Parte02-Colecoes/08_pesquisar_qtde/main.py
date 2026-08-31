paises = [
    "Brasil", 
    "Estados Unidos"
    "Mexico",
    "Argentina",
    "Brasil",
    "Argentina", 
    "Arabia Saudita",
    "ira",
    "Brasil", 
    "Mexico",
    "Estados Unidos",
    "Brasil",
]

pais = input("Informe o pais a ser pesquisada: ").strip().title()

# armazena a qunditdade ocorrencias na lista
qtde = paises.count(pais)

print(f"{pais} foi encontrado {qtde} vezes na lista.")
