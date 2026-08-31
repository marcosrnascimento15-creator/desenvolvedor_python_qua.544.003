# dicionário
usuario = {
    'nome': "Marcos Rodrigues",
    'idade': 35,
    'email': "fulano@gmail.com",
    'cpf': "123.456.789-12"
}

# exibe os dados na tela
# forma 1
print(f"Nome: {usuario['nome']}")
print(f"Idade: {usuario['idade']}")
print(f"email: {usuario['email']}")
print(f"cpf: {usuario['cpf']}")

print("--------------------------------------------------")

# forma 2
print(f"Nome: {usuario.get('nome')}")
print(f"Idade: {usuario.get('idade')}")
print(f"email: {usuario.get('email')}")
print(f"cpf: {usuario.get('cpf')}")


print("---------------------------------------------------")

# forma 3
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

print("---------------------------------------------------------------------------------------------")

# forma 4
print(usuario)