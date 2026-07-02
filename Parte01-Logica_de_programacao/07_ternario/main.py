# Declaracao de variaveis
nome = input("Informe seu nome: ").title()
idade = int(input("Informe sua idade: "))

# Saida de dados com operador ternario
print(f"{nome} é maior de idade." if idade >= 18 else f"{nome} é menor de idade")