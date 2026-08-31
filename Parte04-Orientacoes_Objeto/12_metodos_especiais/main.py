import os
from models import Pessoa

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    pessoa = Pessoa(nome="", idade=0, altura=0.0)

    pessoa.nome = input("Digite o nome da pessoa: ").strip().title()
    pessoa.idade = int(input("Digite a idade da pessoa: ").strip())
    pessoa.altura = float(input("Digite a altura da pessoa (em metros): ").strip())
    
    clear_screen()
    print("\nInformações da pessoa:")
    print(pessoa)
    del pessoa  
    
if __name__ == "__main__":
    main()