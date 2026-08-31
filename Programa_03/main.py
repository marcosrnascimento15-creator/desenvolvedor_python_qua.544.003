# TODO: Atividade 3

"""
Crie um programa que receba uma vez o nome e a idade do usuário, e em seguida mostre os filmes em cartaz em 5 salas de cinema:
- A Volta dos Que Não Foram (livre)
- A Roda Quadrada (12 anos)
- As Tranças do Rei Careca (14 anos)
- Poeira em Alto Mar (16 anos)
- A Vingança do Frango Assado (18 anos)
O usuário irá escolher a sala onde o filme desejado está passando. Caso o usuário não tenha idade, o programa 
impede sua entrada e re-exibe a lista para que o mesmo possa escolher outro filme. Caso o usuário tenha a 
idade mínima, o programa grava em arquivo o bilhete do filme e encerra o programa.
"""

# Entrada de dados
print("---BEM-VINDO AO CINEMA---")

nome = input("Digite seu nome: ").strip()
idade = float(input("Digite sua idade: "))


while True:
    print("--------------------------------------------------")
    print("Salas de Exibição")
    print("Sala 01: A Volta do que Não Foram (Livre)")
    print("Sala 02: A Roda Quadrada (12 anos)")
    print("Sala 03: As Tranças do Rei Careca (14 anos)")
    print("Sala 04: Poeira em Alto Mar (16 anos)")
    print("Sala 05: A Vingança do Frango Assado (18 anos)")
    print("--------------------------------------------------")
    
    sala = int(input("Digite o numero da sala desejada (1-5) "))

    if sala == 1:
        titulo = "A Volta dos que não foram (Livre)"
        idade_minima = 0
    elif sala == 2:
        tituloitulo = "A Roda Quadrada (12 anos)"
        idade_minima = 12
    elif sala == 3:
        titulo = "As Tranças do Rei Careca (14 anos)"
        idade_minima = 14
    elif sala == 4:
        titulo = "Poeira em Alto Mar (16 anos)"
        idade_minima = 16
    elif sala == 5:
        titulo = "A Vingança do Frango Assado (18 anos)"
    else:
        print("Opção inválida escolha um numero de 1-5")
        continue
    if idade < idade_minima:
        print("===========================================")
        print("")