import pyautogui as auto
import pyperclip
import time
from datetime import date


def hoje():
    return date.today().strftime("%d/%m/%Y")

def colar_texto(texto):
    """Copia o texto para a área de transferência e cola para evitar erros de teclado ABNT2."""
    pyperclip.copy(texto)
    auto.hotkey('ctrl', 'v')

def main():
    auto.PAUSE = 0.75

    auto.press('win')
    auto.write('git bash')
    auto.press('enter')
    
    # Substituído auto.sleep por time.sleep
    time.sleep(5) 

    # Usado r"..." (Raw String) com barras normais para o Git Bash
    caminho = r"C:/Users/ALUNO/Marcos_R_Nascimento/desenvolvedor_python_qua.544.003"
    colar_texto(f'cd "{caminho}"')
    auto.press('enter')

    colar_texto("git add .")
    auto.press('enter')

    # Usando a função colar_texto para garantir a digitação das aspas e das barras da data
    colar_texto(f'git commit -m "Commit do dia {hoje()}"')
    auto.press('enter')

    colar_texto("git push")
    auto.press('enter')


if __name__ == "__main__":
    main()
    