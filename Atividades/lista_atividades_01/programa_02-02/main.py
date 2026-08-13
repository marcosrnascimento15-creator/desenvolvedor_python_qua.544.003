#TODO: Atividade 02
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

# 1. Entrada de dados do usuário
print("=== BEM-VINDO AO CINEMA ===")
nome = input("Digite seu nome: ").strip()

# Validação da idade
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Por favor, digite uma idade válida.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros para a idade.")

# 2. Loop principal para escolha da sala
while True:
    # Exibição do menu de filmes
    print("----------------------------------------------------")
    print("--- FILMES EM CARTAZ ---")
    print("Sala 1: A volta dos que não foram (Classificação: Livre)")
    print("Sala 2: A roda quadrada (Classificação: 12 anos)")
    print("Sala 3: As Tranças do Rei Careca (Classificação: 14 anos)")
    print("Sala 4: Poeira em Alto Mar (Classificação: 16 anos)")
    print("Sala 5: A vingança do Frango Assado (Classificação: 18 anos)")
    print("--------------------------------------------------")

    # Leitura da escolha
    try:
        sala = int(input("\nDigite o número da sala desejada (1-5): "))
    except ValueError:
        print("\n[!] Entrada inválida! Digite apenas o número da sala.")
        continue

    # 3. Verificação da sala e da idade mínima
    if sala == 1:
        titulo = "A volta dos que não foram"
        idade_minima = 0
    elif sala == 2:
        titulo = "A roda quadrada"
        idade_minima = 12
    elif sala == 3:
        titulo = "As Tranças do Rei Careca"
        idade_minima = 14
    elif sala == 4:
        titulo = "Poeira em Alto Mar"
        idade_minima = 16
    elif sala == 5:
        titulo = "A vingança do Frango Assado"
        idade_minima = 18
    else:
        print("\n[!] Sala inválida! Escolha um número de 1 a 5.")
        continue

    # 4. Checagem se a idade do usuário permite assistir ao filme
    if idade < idade_minima:
        # Exibimos explicitamente a sala escolhida e a mensagem de erro bem visível:
        print("\n==================================================")
        print(f"[X] VOCÊ ESCOLHEU A SALA {sala} ('{titulo}')")
        print(f"[X] ENTRADA PROIBIDA! Sua idade ({idade} anos) é menor que a idade mínima ({idade_minima} anos).")
        print("Por favor, escolha um filme adequado para a sua faixa etária abaixo:")
        print("==================================================")
    else:
        # Idade permitida: grava o bilhete e encerra
        print(f"\n[✓] Ingresso liberado! Bom filme, {nome}!")

        # Monta o texto do bilhete
        conteudo_bilhete = (
            "====================================\n"
            "          BILHETE DE CINEMA         \n"
            "====================================\n"
            f"Cliente: {nome}\n"
            f"Idade: {idade} anos\n"
            f"Sala: {sala}\n"
            f"Filme: {titulo}\n"
            f"Classificação: {idade_minima} anos\n"
            "====================================\n"
        )

        # Grava no arquivo bilhete.txt
        with open("bilhete.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo_bilhete)

        print("Seu bilhete foi gravado com sucesso no arquivo 'bilhete.txt'.")
        break