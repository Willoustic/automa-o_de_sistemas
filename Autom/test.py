import pyautogui as px
from pyperclip import paste
from time import sleep
from verificar import lista
import shutil, os

#abrir google
px.click(658,870, duration=0.2)
sleep(1)

# abrir download
px.hotkey('ctrl', 'j')
sleep(3)
# pegar o nome do arquivo
px.moveTo(467,238, duration=1)
px.mouseDown(button='left')
px.moveTo(649,236, duration=1)
px.mouseUp(button='left')
px.hotkey('ctrl', 'c')


nome_do_arquivo = paste()
print(nome_do_arquivo)

#print(f'{nome_do_arquivo}')
caminho = f'C:\\Users\\WELTON\\Downloads\\{nome_do_arquivo}'
caminho_atual = os.getcwd()

shutil.move(f"{caminho}",f"{caminho_atual}\\{nome_do_arquivo}x")
