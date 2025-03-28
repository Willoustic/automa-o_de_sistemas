import pandas as pd
import xlrd as xl
import pyautogui as px
from time import sleep

nome_relatorio = 'C:\\Users\\POSTO NH\\Desktop\\Carlos\\documentos\\testes\\App\\Autom\\Planilha da Automação.xlsx'

lista = list()

def rela():
    try:
        rel = pd.read_excel(nome_relatorio, index_col=False)
    except:
        pass
    finally:
        return rel
    


def auto(rel):    
    placas = rel['Autorização']
    valores = rel['Valor']
    lista1 = []
    for pos_placa, placa in enumerate(placas):
        try:
            placa = str(f'{float(placa):.0f}')
        except:
            pass
        
        for pos_valor, valor in enumerate(valores):
            if pos_valor == pos_placa:
                dic = {
                    'Placa': f'{placa}',
                    'Valor': valor,
                    'Operador': ''
                }
                lista1.append(dic)

    return lista1


def verificar_dados(dado):
    from datetime import datetime
    print('=+' * 20)
    print('')
    print(f'Dados informados às {datetime.now().strftime("%H:%M:%S")} de {datetime.now().day}/{datetime.now().month}/{datetime.now().year}: ')
    print('')
    for dados in dado:
        try:
            print(f"""Aut: {dados['Placa']} | Valor: {float(dados['Valor']):.2f}""")
        except:
            print('Dados informados incorretamente')
    print('')
    print('=+' * 20)
    print('')
    print('Programa finalizado')

relatorio = rela()
lista = auto(relatorio)
#verificar_dados(lista)