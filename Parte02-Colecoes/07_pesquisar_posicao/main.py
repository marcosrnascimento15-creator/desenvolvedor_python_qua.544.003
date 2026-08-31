cidades = [
    "Brasília",
    "Rio de Janeiro",
    "São Paulo",
    "Belo Horizonte",
    "Goiania", 
    "Manaus",
    "Fortaleza",
    "Florianopolis",
]

cidade = input("Informe a cidade a ser pesquisada: ").strip().title()

# mostra a posição do item na lista
if cidade in cidades:
    indice = cidade.index(cidade)
    print(f"Indice de {cidade}na lista é {indice}")
else:
    print("Cidade não encontrada.")
    