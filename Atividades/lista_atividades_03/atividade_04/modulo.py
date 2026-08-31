import math
import os

def limpar_terminal():
    # Limpa tela
    os.system("cls" if os.name == "nt" else "clear")

def calcular_potencia(base, expoente):
    # base e expoente
    return base**expoente

def calcular_raiz_quadrada(numero):
    # raiz quadrada
    if numero < 0:
        return "Erro: Não existe raiz real para número negativo."
    return math.sqrt(numero)

def volume_paralelepipedo(comprimento, largura, altura):
    # Calcula o volume de um recipiente paralelepípedo (V = c * l * a)
    return comprimento * largura * altura


def volume_cilindro(raio, altura):
    # Calcula o volume de um recipiente cilíndrico (V = π * r² * h)
    return math.pi * (raio**2) * altura

