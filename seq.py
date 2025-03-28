from login import tela_de_login
from opções import opções
from time import sleep

def app():
    sit = tela_de_login()
    if sit == True:
        sleep(2)
        opções()
        
        


