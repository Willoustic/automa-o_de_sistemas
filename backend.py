import os
import pandas as pd


nome_do_bd = 'C:\\Users\\POSTO NH\\Desktop\\Carlos\\documentos\\testes\\App\\Banco\\bancodedados.txt'
banco_dic = []
banco_nomes = []

def bancobd():
    if os.path.exists(nome_do_bd):
        banco = open(nome_do_bd, 'r+')
    else:
        banco = open(f'{nome_do_bd}', 'w')
        banco = open(nome_do_bd, 'r+')
    
    return banco


def atualizar_banco(banco):
    banco_dici = []
    for usuario_cadastrado in banco.split('.'):
        #print(usuario_cadastrado)
        usuario_cadastrado = usuario_cadastrado.replace('\n', '')
        usuario_cadastrado = usuario_cadastrado.replace('/n', '')
        usuario_db = usuario_cadastrado.split(';')
        if usuario_db == ['']:
            pass
        else:
            nome_db = usuario_db[0]
            senha_db = usuario_db[1]
            banco_dici.append({
                'Nome': nome_db,
                'Senha': senha_db
            }) 

    return banco_dici
        

def atualizar_nomes(bd):
    banco_nome = []
    try:
        for l, k in enumerate(bd):
            banco_nome.append(str(k['Nome']).strip().lower().capitalize())
    except:
        pass
    finally:
        return banco_nome
    
bancodb = bancobd()
banco_dic = atualizar_banco(bancodb.read())
banco_nomes = atualizar_nomes(banco_dic)
