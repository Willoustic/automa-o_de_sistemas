import pyautogui as px
from time import sleep
import shutil, os
from pyperclip import paste

px.click(665,468)
px.mouseDown(663,489)
sleep(1)
px.mouseUp()
px.hotkey('alt', 'tab')


def proximo():
    sleep(1)
    px.click(641,102, duration=0.5)
    sleep(3)

def rateio_ctf(valor):
    cont = 1
    while cont <= valor:
        sleep(0.5)
        #responsaveis
        px.click(380,199, duration=0.5)
        #rateio
        px.doubleClick(825,648, duration=0.5)
        sleep(0.5)
        px.hotkey('ctrl', 'c')
        rateio = paste()
        #incluir
        px.click(546,163, duration=0.5)
        # inserir codigo 1661
        px.write('1661')
        px.press('enter')
        sleep(1)
        #inserir rateio
        px.doubleClick(894,323)
        px.write(rateio)
        sleep(0.5)
        #observarção
        px.click(613,301, duration=0.3)
        px.write('REF A VENDA CTF')
        #incluir
        px.click(476,218, duration=0.5)
        sleep(1.5)
        #fechar aba:
        px.click(894,185, duration=0.5)
        sleep(1.3)
        #clicar salvar
        px.click(357,103, duration=0.5)
        sleep(5)
        px.press('enter')
        sleep(1)
        #proximo
        proximo()
        sleep(1)
        cont += 1


    

