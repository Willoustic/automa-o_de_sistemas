import pyautogui as px
from time import sleep

def excluir_(valor):
    cont = 1
    while cont <= valor:
        if cont == 1:
            px.click(652,744, duration=0.5)
            sleep(0.5)
        px.click(358,134, duration=0.5)
        sleep(0.5)
        px.click(360,276, duration=0.5)
        sleep(0.8)
        if cont == 1:
            px.click(753,168, duration=0.5)
            sleep(0.5)
        px.click(702,168, duration=0.5)
        sleep(1)
        px.click(358,98, duration=0.5)
        sleep(3)
        px.press('esc')
        sleep(1)
        px.click(644,103, duration=0.5)
        sleep(6)
    
        cont += 1

