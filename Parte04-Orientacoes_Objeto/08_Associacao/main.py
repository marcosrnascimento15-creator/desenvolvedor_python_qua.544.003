import os

from models import Endereco, Pessoa

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    endereco = Endereco(uf="SP", cidade="São Paulo")
    usuario = Pessoa(nome="João", endereco=endereco)
    usuario.apresentar_endereco()

    clear_screen()
    usuario.nome = input("Digite o novo nome do usuário: ").strip().title()
    usuario.endereco.uf = input("Digite a nova UF do endereço: ").strip().upper()
    usuario.endereco.cidade = input("Digite a nova cidade do endereço: ").strip().title()
    print("\nInformações atualizadas:")
    usuario.apresentar_endereco()

if __name__ == "__main__":
    main()