import pyautogui as px
from time import sleep

def salvar(valor):
    cont = 1
    while cont <= valor:
        print(cont)
        if cont == 1:
            print("abrir programa")
            px.click(648,746, duration=0.5)
            print("desbugar")
            px.click(370,131)
        print('salvar')
        px.click(356,114, duration=0)
        sleep(3)

        print('clicar enter pra confirmar fechamento')
        px.press('enter')
        sleep(1)
        
        if cont < valor:
            print('proximo')
            px.click(645,100, duration=0.2)
            sleep(3)

        print(f'{cont}º procedimento finalizado')
        print('=+' * 30)
        print('')
        cont += 1
    
    print('fim do funcionamento ')
    print('')




