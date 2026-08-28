import os
from models import Pedido

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    pedido = Pedido(0, 0)
    pedido.valor1 = float(input("Digite o primeiro valor: ").strip())
    pedido.valor2 = float(input("Digite o segundo valor: ").strip())
    operador = input("Escolha a operação (1 - somar, 2 - subtrair, 3 - multiplicar, 4 - dividir): ").strip()

    clear_screen()

    resultado = pedido.calcular_total(operador)

    clear_screen()
    print(f"\nResultado da operação {operador}: {resultado}")

if __name__ == "__main__":
    main()