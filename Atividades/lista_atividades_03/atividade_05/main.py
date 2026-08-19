import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def fibonacci(n):
    # Retorna o n-ésimo termo da sequência de Fibonacci, usando recursividade
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def gerar_sequencia(qtd_termos):
    # Gera e imprime a sequência de Fibonacci até a quantidade de termos informada
    sequencia = []
    for i in range(qtd_termos):
        sequencia.append(fibonacci(i))
    return sequencia

# Programa principal
limpar()    
print("-=-=-=-=-=-=-=-=-=Sequencia Fibonacci-=-==-=-=-=-=-=-=-=-=-=")
numero = int(input("Digite um número inteiro (quantidade de termos): "))

if numero < 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    resultado = gerar_sequencia(numero)
    print(f"Sequência de Fibonacci até {numero} termos:")
    print(resultado)
    print("==================================================")
    print("Criado e desenvolvido por Marcos R. Nascimento")
    