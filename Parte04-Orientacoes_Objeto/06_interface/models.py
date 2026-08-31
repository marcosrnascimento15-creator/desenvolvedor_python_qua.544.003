from abc import ABC, abstractmethod

# 1. Nome corrigido para IConta (C maiúsculo)
class IConta(ABC):
    @abstractmethod 
    def consultar_conta(self):
        pass

    # 2. Inclusão do 'self' na assinatura dos métodos
    @abstractmethod
    def fazer_deposito(self, valor):
        pass

    @abstractmethod
    def fazer_saque(self, valor):
        pass


class Conta(IConta):
    def __init__(self, titular, cpf, agencia, n_conta, saldo=0.0):
        self.__titular = titular
        self.__cpf = cpf
        self.__agencia = agencia
        self.__n_conta = n_conta
        self.__saldo = saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def agencia(self):
        return self.__agencia

    @property
    def n_conta(self):
        return self.__n_conta

    # Mantemos apenas o getter do saldo para proteger o atributo contra alterações diretas
    @property
    def saldo(self):
        return self.__saldo

    def consultar_conta(self):
        print(f"Nome do titular: {self.__titular}")
        print(f"CPF do titular: {self.__cpf}")
        print(f"Agência: {self.__agencia}")
        print(f"Número da conta: {self.__n_conta}")
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

    def fazer_deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def fazer_saque(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False