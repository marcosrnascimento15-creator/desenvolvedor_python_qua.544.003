# função recursiva para calcular fatorial
def fatorial(n):
    return 1 if n == 0 else n * fatorial(n-1)

# programa principal
def main():
    n = int(input("Informe um numero inteiro: "))
    print(f"O fatorial de {n} é {fatorial(n)}.")

if __name__ == "__main__":
    main()