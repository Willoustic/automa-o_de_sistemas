import pyautogui as px
from time import sleep

def fechamento(valor):
    cont = 1
    while cont <= valor:
        print(cont)
        if cont == 1:
            print("abrir programa")
            px.click(648,746, duration=0.2)
            print("tirar da tela as janelas")
            px.click(370,131)
        sleep(0.5)
        print("clicar para confirmar o primeiro caixa")
        px.click(761,641, duration=0.2)
        sleep(1)
        print("clicar em confirmar o fechamento do caixa")
        px.write("y")
        sleep(5)
        print("clicar para finalizar")
        px.press("enter")
            
        if cont < valor:
            sleep(5)
            print("proximo caixa")
            px.click(638,102, duration=0.2)
            sleep(5)

        cont += 1
    print('fim da execução!')

