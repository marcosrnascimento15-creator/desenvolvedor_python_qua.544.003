import pyjokes
from deep_translator import GoogleTranslator

import os


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_piada():
    tradutor = GoogleTranslator(source='en', target='pt')
    piada = pyjokes.get_joke()
    return tradutor.translate(piada)

def traduzir_piada(piada, idioma):
    traducao = GoogleTranslator(source_lang="pt", target_lang=idioma).translate(piada)
    return traducao

def main():
    limpar()
    while True:
        print("=== Gerador de Piadas ===")
        print("0 - Sair do programa")   
        print("1 - Gerar nova piada")
        opcao = input("Escolha uma opção: ").capitalize()
        if opcao == "0":
            print("Saindo do programa...")
            break
        elif opcao == "1":
            piada = gerar_piada()
            print(f"\nPiada gerada: {piada}\n")
            idioma = input("Digite o idioma para tradução (ex: pt, es, fr): ").lower()
            traducao = traduzir_piada(piada, idioma)
            print(f"Tradução: {traducao}\n")
        else:
            print("Opção inválida. Tente novamente.\n")
        continue_prompt = input("Deseja continuar? (s/n): ").lower()
        if continue_prompt != 's':
            print("Saindo do programa...")
            break

if __name__ == "__main__":
    main()