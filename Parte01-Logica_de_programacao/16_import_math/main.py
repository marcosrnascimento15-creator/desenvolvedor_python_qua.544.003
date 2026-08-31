# Importação de bibliotecas
import math

# tratamento de exceção
try:
    while True:
        # usuario informa valor do raio
        r = float(input("Informe o valor do raio em m²: ").replace(",","."))

        # calcula a area do circulo
        area = math.pi*r**2

        # imprime na tela a area do circulo
        print(f"Área do círculo: {area:.2f} m².")

        # usuario informa se deseja continuar ou não
        print("1 - Calcular área de outro circulo")
        print("2 - Sair do programa")

        opcao = input("Informe sua opção: ").strip()

        match opcao:
            case "1":
                continue
            case '2':
                break
            case _:
                print("Opção Inválida.")
                continue
except Exception as e:
    print("Não foi possível calcular. {e}")