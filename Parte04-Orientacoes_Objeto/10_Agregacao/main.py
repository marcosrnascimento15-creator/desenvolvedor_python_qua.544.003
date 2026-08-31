import os
from models import Departamento, Empresa

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    departamento = Departamento(nome="Recursos Humanos")
    empresa = Empresa(nome="Tech Solutions", departamento=departamento)

    clear_screen()

    empresa.nome = input("Digite o nome da empresa: ").strip().title()
    empresa.departamento.nome = input("Digite o nome do departamento: ").strip().title()
    clear_screen()
    print("\nInformações da empresa:")
    print(empresa.detalhes())

if __name__ == "__main__":
    main()