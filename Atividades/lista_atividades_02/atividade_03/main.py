import os
import json

os.system("cls" if os.name == "nt" else "clear")
# Nota aluno
ARQUIVO_JSON = "alunos.json"

while True:
    print("======================CADASTRO DE ALUNO====================================")
    
    # recebe nome do aluno
    nome = input("Informe o nome do aluno: ").strip().title()

    # recebe 3 notas do aluno e armazena em uma lista
    notas = []
    for i in range(1, 4):
        nota = float(input(f"Informe a {i}ª nota do aluno: ").strip())
        notas.append(nota)

    # calcula a média do aluno
    media = sum(notas) / len(notas)

    # Verifica se o aluno esta aprovado ou reprovado
    situacao = "Aprovado" if media >= 7 else "Reprovado"

    # resultado da nota
    print(f"\nMédia: {media:.2f}")
    print(f"Situação: {situacao}\n")

    usuario = {
        'Aluno': "",
        'Nota': ""
    }
    
