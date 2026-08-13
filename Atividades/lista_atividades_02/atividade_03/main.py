import json
import os

ARQUIVO_JSON = "alunos.json"

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("========================aluno cadastro notas========================")
   
    # recebe nome do aluno
    nome = input("Informe o nome do aluno: ").strip().title()

    # coleta as 3 notas do aluno e armazena 
    notas = []
    for i in range(1, 4):
        nota = float(input(f"Informe a {i}ª nota do aluno: ").strip())
        notas.append(nota)

    # calcula a média do aluno
    media = sum(notas) / len(notas)

    # verifica se o aluno está aprovado ou reprovado
    situacao = "Aprovado" if media >= 7 else "Reprovado"

    # exibe o resultado
    print(f"\nMédia: {media:.2f}")
    print(f"Situação: {situacao}\n")

    # cria o dicionário
    aluno = {
        'nome': nome,
        'notas': notas,
        'media': round(media, 2),
        'situacao': situacao
    }

    # JSON gravação
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            dados = json.load(f)
    else:
        dados = []

    # insere o novo aluno
    dados.append(aluno)

    # grava a lista
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f,)

    print("Dados do aluno salvos com sucesso no arquivo JSON!\n")

    # pergunta ao usuário se deseja cadastrar outro aluno
    opcao = input("Deseja inserir os dados de outro aluno? (S/N): ").strip().upper()
    if opcao != "S":
        print("\nPrograma finalizado.")
        break