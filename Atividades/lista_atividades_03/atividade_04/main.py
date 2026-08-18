import modulo as m


def menu():
    while True:
        print("\n=== MENU DE OPÇÕES ===")
        print("1 - Limpar o terminal")
        print("2 - Calcular potência")
        print("3 - Calcular raiz quadrada")
        print("4 - Calcular volume de um paralelepípedo")
        print("5 - Calcular volume de um cilindro")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            m.limpar_terminal()

        elif opcao == "2":
            base = float(input("Digite a base: "))
            expoente = float(input("Digite o expoente: "))
            resultado = m.calcular_potencia(base, expoente)
            print(f"Resultado: {base} elevado a {expoente} = {resultado}")

        elif opcao == "3":
            num = float(input("Digite o número: "))
            resultado = m.calcular_raiz_quadrada(num)
            print(f"Resultado: {resultado}")

        elif opcao == "4":
            comp = float(input("Digite o comprimento: "))
            larg = float(input("Digite a largura: "))
            alt = float(input("Digite a altura: "))
            vol = m.volume_paralelepipedo(comp, larg, alt)
            print(f"Volume do paralelepípedo: {vol:.2f}")

        elif opcao == "5":
            raio = float(input("Digite o raio da base: "))
            alt = float(input("Digite a altura: "))
            vol = m.volume_cilindro(raio, alt)
            print(f"Volume do cilindro: {vol:.2f}")

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()