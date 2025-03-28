import pyautogui as px
from time import sleep

def excluir_sangria(valor):
    cont = 1
    while cont <= valor:
        print(cont)
        if cont == 1:
            print("#abrir programa")
            px.click(648,746, duration=1)
            print("desbugar")
            px.click(370,131)
        
        print('clicar no + de recebimento')
        px.click(316,185, duration=0.5)
        sleep(0.5)

        print('clicar em especie')
        px.click(383,197, duration=0.5)
        sleep(0.5)

        print('clicar em excluir')
        px.click(679,163, duration=0.5)
        sleep(0.5)

        print('confirmar exclusão')   
        px.write('y')
        sleep(1)

        print('salvar')
        px.click(356,114, duration=0.5)
        sleep(3)

        print('clicar enter pra confirmar fechamento')
        px.press('enter')
        sleep(1)
        
        if cont < valor:
            print('proximo')
            px.click(645,100, duration=0.5)
            sleep(5)

        print(f'{cont}º procedimento finalizado')
        print('=+' * 30)
        print('')
        cont += 1
    
    print('fim do funcionamento ')
    print('')
