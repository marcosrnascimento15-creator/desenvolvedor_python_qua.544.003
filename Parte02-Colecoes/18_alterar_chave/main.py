usuario = {
    'nome': "Alex Machado",
    'idade': 41,
    'profissão': "desenvolvedor"
}

# alterando os dados de uma chave
usuario['profissão'] = 'gerente de projetos'

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")