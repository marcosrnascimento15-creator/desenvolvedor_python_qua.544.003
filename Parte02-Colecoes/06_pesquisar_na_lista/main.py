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
cidade_pesquisada = input("Informe o nome a ser pesquisa: ").strip().title()

# busca pelo nome desejado e informa o resultado
print(f"{cidade_pesquisada} econtrada." if cidade_pesquisada  in cidades else f"Cidade não encontrada")