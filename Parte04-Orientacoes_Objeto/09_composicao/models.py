class Motor:
    def __init__(self, potencia):
        self.__potencia = potencia

    def ligar(self):
        print(f"Motor de {self.potencia} HP ligado.")

    def desligar(self):
        print("Motor desligado.")

    @property
    def potencia(self):
        return self.__potencia

    @potencia.setter
    def potencia(self, potencia):
        self.__potencia = potencia

class Carro:
    def __init__(self, modelo, potencia):
        self.__modelo = modelo
        self.__motor = Motor(potencia)

    def ligar_motor(self):
        self.__motor.ligar()

    def desligar_motor(self):
        self.__motor.desligar()

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self, motor):
        self.__motor = motor

    def detalhes(self):
        return f"Carro: {self.__modelo}, Motor: {self.__motor.potencia} HP"