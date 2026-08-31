from modulo import limpar, soma, subtrair

def main():
    limpar()
    x = int(input("Informe o valor de x: "))
    y = int(input("Informe o valor de y: "))
    limpar()
    print(f"O valor de soma é :{soma(x, y)}")
    print(f"O valor da subtração é: {subtrair(x, y)}")

if __name__=="__main__":
    main()