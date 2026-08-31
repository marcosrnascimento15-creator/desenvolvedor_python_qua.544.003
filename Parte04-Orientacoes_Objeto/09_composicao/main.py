import os
from models import Carro

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    carro = Carro(modelo="Fusca", potencia=50)

    carro.modelo = input("Digite o modelo do carro: ").strip().title()
    carro.motor.potencia = int(input("Digite a potência do motor (HP): ").strip())
    clear_screen()
    print("\nInformações do carro:")
    print(carro.detalhes())

if __name__ == "__main__":
    main()