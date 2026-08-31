class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero não é permitida."

class Pedido:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    @property
    def valor1(self):
        return self.__valor1

    @property
    def valor2(self):
        return self.__valor2

    @valor1.setter
    def valor1(self, valor1): 
        self.__valor1 = valor1

    @valor2.setter
    def valor2(self, valor2):   
        self.__valor2 = valor2

    def calcular_total(self, operador):
        calc = Calculadora()
        match operador:
            case '1':
                return calc.soma(self.__valor1, self.__valor2)
            case '2':
                return calc.subtracao(self.__valor1, self.__valor2)
            case '3':
                return calc.multiplicacao(self.__valor1, self.__valor2)
            case '4':
                return calc.divisao(self.__valor1, self.__valor2)
            case _:
                return "Operador inválido. Use '+', '-', '*' ou '/'."   
        return math_operations.get(operador, lambda a, b: "Operador inválido. Use '+', '-', '*' ou '/'.")(self.__valor1, self.__valor2) 