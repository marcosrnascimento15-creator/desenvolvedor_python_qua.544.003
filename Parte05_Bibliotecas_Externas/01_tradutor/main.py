from deep_translator import GoogleTranslator

import os


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def traduzir(texto, idioma_destino):
    tradutor = GoogleTranslator(source='auto', target=idioma_destino)
    return tradutor.translate(texto)

def main():
    limpar()
    while True:
        print("0 - Sair do programa")
        print("1 - Traduzir texto para português")
        opcao = input("Escolha uma opção: ")

        limpar()

        if opcao == "0":
            print("Saindo do programa...")
            break
        elif opcao == "1":
            texto = input("Digite o texto a ser traduzido: ")
            idioma_destino = "pt"
            traducao = traduzir(texto, idioma_destino)
            print(f"Texto traduzido: {traducao}")


if __name__ == "__main__":
    main()
