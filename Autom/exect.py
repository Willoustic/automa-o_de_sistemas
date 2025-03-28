from execução import executar, rateio_ctf
import pyautogui as px
from time import sleep




def programa_completo(valor):
    executar(valor)
    # voltar todos os caixas
    px.click(579,103)
    sleep(5)
    rateio_ctf(valor)



