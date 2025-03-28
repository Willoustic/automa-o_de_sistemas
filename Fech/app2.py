import pyautogui as px
import pyperclip as pc
from time import sleep


def inserir_rateio(valor):
    cont = 1
    while cont <= valor:
        print(f'Valor inserido: {valor}')
        if cont == 1:
            print("abrir programa")
            px.click(648,746, duration=0.5)

        print("desbugar")
        px.doubleClick(357,132, duration=0.5)

        print("pegar usuário")
        px.doubleClick(653,197, duration=0.5)
        px.hotkey('ctrl', 'c')
        operador = pc.paste()
        print(f'operador: {operador}')
        sleep(0)

        print('clicar em responsaveis')
        px.click(372,198, duration=0.5) #responsaveis
        sleep(1)
        print("pegar rateio")
        px.doubleClick(825,649, duration=0.5)
        sleep(1)
        px.hotkey('ctrl', 'c')
        rateio = pc.paste()
        if rateio == '0':
            print('Rateio = 0,00')
        else:
            print(f'rateio: {rateio}')
            sleep(0)
            print('clicar em incluir')
            px.click(549,164, duration=0.5) #incluir
            sleep(1)
            print('colocar op')
            #px.doubleClick(557,273, duration=1) #colocar op
            sleep(0.5)
            px.write(operador)
            px.press("enter")
            sleep(0.5)
            print('colocar valor rateio')
            px.doubleClick(894,327, duration=0.5) #colocar valor rateio
            sleep(0.5)
            px.write(rateio)
            sleep(0.5)
            print('incluir')
            px.click(472,217, duration=0.5) #incluir)
            sleep(0.5)
            print('fechar aba')
            px.click(890,184, duration=0.5) #fehcar aba)
            sleep(0.5)
        print('salvando')
        px.click(357,98, duration=0.5) #salvar
        sleep(3)
        px.press("enter")
        print('próximo')
        px.click(640,101, duration=0.2) # clicar pro proximo
        print(f'{cont}º operador: {operador} com rateio {rateio} finalizado')
        cont += 1
        sleep(3)
    print('fim da execução!')

