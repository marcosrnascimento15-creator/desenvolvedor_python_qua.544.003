from abc import ABC, abstractmethod
import json


class IConta(ABC):
    @abstractmethod
    def consultar_dados(self):
        pass

    @abstractmethod
    def gerar_extrato(self):
        pass

    @abstractmethod
    def depositar(self, valor: float) -> float:
        pass

    @abstractmethod
    def sacar(self, valor: float) -> float:
        pass

class Pessoa:
    def __init__(self, nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    def __str__(self) -> str:
        return f"Nome: {self.__nome} | CPF: {self.__cpf}"


class Conta(IConta):
    def __init__(self, titular: Pessoa, agencia: str, n_conta: str, saldo: float = 0.0):
        self.__titular = titular
        self.__agencia = agencia
        self.__n_conta = n_conta
        self.__saldo = saldo

    @property
    def titular(self) -> Pessoa:
        return self.__titular

    @titular.setter
    def titular(self, titular: Pessoa):
        self.__titular = titular

    @property
    def agencia(self) -> str:
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia: str):
        self.__agencia = agencia

    @property
    def n_conta(self) -> str:
        return self.__n_conta

    @n_conta.setter
    def n_conta(self, n_conta: str):
        self.__n_conta = n_conta

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo: float):
        self.__saldo = saldo

    def consultar_dados(self) -> None:
        print(f"====== Dados da Conta ======")
        print(f"Titular: {self.__titular.nome}")
        print(f"CPF: {self.__titular.cpf}")
        print(f"Agência: {self.__agencia}")
        print(f"Número da Conta: {self.__n_conta}")

    def gerar_extrato(self) -> None:
        print(f"====== Extrato ======   ")
        print(f"Titular: {self.__titular.nome}")
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

    def depositar(self, valor: float) -> float:
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")
        return self.__saldo

    def sacar(self, valor: float) -> float:
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")
        return self.__saldo
    
