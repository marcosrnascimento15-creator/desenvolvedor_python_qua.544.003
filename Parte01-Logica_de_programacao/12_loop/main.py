# tratamento de excecao
try:
    # usuario informa numero inteiro
    n = int(input("Informe um numero inteiro: "))

    # laço de repetição
    while n >= 0:
        print(n)
        n -= 1
except:
    print("Não foi possível exibir a mensagem.")