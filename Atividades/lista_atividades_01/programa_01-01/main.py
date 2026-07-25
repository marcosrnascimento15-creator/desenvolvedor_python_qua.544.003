#TODO: atividade 01
"""
Crie um programa que receba o nome, peso e altura do usuario e informe na tela o seu IMC o seu diagnostico com base no valor do IMC
"""
import os

# Limpa a tela
os.system("cls" if os.name == "nt" else "clear")
print("Calculador IMC")

 
# Entrada de dados
nome = input("Digite seu nome: ").title()
peso = float(input("Digite seu peso em kg: ").replace(",", "."))
altura = float(input("Digite sua altura em metros: ").replace(",", "."))

imc = peso / (altura ** 2)

if imc < 18.5:
    diagnostico = "Abaixo do peso"
elif imc < 25.0:
    diagnostico = "Peso normal"
elif imc < 30.0:
    diagnostico = "Sobrepeso"
elif imc < 35.0:
    diagnostico = "Obesidade Grau I"
elif imc < 40.0:
    diagnostico = "Obesidade Grau II"
else:
    diagnostico = "Obesidade Grau III (Mórbida)"
    
os.system("cls" if os.name == "nt" else "clear")

print("\n--- Resultado ---")
print(f"Nome: {nome}")
print(f"IMC: {imc:.2f}")
print(f"Diagnóstico: {diagnostico}")

