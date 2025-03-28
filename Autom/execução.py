import pyautogui as px
from pyperclip import paste
from time import sleep
from .verificar import auto, rela


def executar(valor):
    cont = 1
    
    relatorio = rela()
    lista = auto(relatorio)

    qtd = len(lista)
    operadores = []
    print(f'Qtd. de caixas a fechar: {valor}') 
    while cont <= valor:
        print(f'Placas a pesquisar: {qtd}')
        print(f'{cont}º execução de {valor}')
        print('=+' * 20)       
        if cont == 1:    
            #abrir programa:
            px.click(649,747, duration=0.5)
            sleep(0.5)
        #desbugar
        px.click(591,662, duration=0.2)
        px.click(354,134, duration=0.2)
        sleep(0.5)
        #pegar operador
        px.doubleClick(643,185, duration=0.2)
        sleep(0.2)
        px.hotkey('ctrl', 'c')
        operador = paste()
        print(F'Operador nº{cont}: {operador}')
        
        if cont == 1:
            #clicar em + de recebimento
            px.click(315,182, duration=0.2)
            sleep(0.2) 
            #clicar em + de duplicata
            px.click(336,228, duration=0.2)
            sleep(0.2)
            #clicar em cartao de credito
            px.click(415,277, duration=0.2)
            sleep(0.2)
        else:
            # clicar em recebimento
            px.click(393,183, duration=0.2)
 
        if cont == 1:
            #clicar na seta de tipo
            px.click(665,468)
            # scrollar pra cima
            px.mouseDown(663,489)
            sleep(1)
            px.mouseUp()
            #clicar pra descer
            px.click(667,539, duration=0.2)
            #clicar em aut pos
            px.click(616,500, duration=0.2)
            sleep(0.2)
            #px.click(357,393, duration=1)
            sleep(0.2)
        

        #--- repetir apartir daqui
        diferencas = list()
        for placa in lista:
        
        #print(f'{placas}ª a verificar')
        #print(placa['Placa'])
        #clicar na barra de pesquisa
            if placa['Operador'] == '':
                px.click(746,471, duration=0.2)
                sleep(0.2)
                px.write(str(placa['Placa']).upper())
                sleep(0.1)
                #clicar em localizar
                px.click(877,468, duration=0.2)
                #press enter
                sleep(0.2)
                px.press('enter')
                sleep(0.5)
                #clicar em alterar
                px.click(595,170, duration=0.5)
                # clicar yes
                px.write('y')
                sleep(1)
                px.press('esc')
                sleep(0.5)
                #doubleclick no valor da autorização (ou seja na placa)
                px.doubleClick(559,489, duration=0.2)
                #px.doubleClick(590,310)
                px.hotkey('ctrl', 'c')
                placa_pesquisada = paste()
                #print(placa_pesquisada)
                #verificar de o valor da placa é a mesma
                #se for:
                if str(placa_pesquisada)[-4:] in str(placa['Placa'])[-4:] :    
                
                    
                    #clicar no valor
                    px.doubleClick(887,350, duration=0.1)
                    sleep(0.5)
                    px.hotkey('ctrl', 'c')
                    valor_antigo = paste()
                    
                
                    if ',' in valor_antigo:
                        valor_antigo = valor_antigo.replace(',', '.')
                        valor_antigo = float(valor_antigo)

                    diferenca = float(placa['Valor']) - float(valor_antigo)
                    diferenca = float(f'{diferenca:.2f}')
                    if float(diferenca) < 50 and float(diferenca) > -50:
                        #adicionar nome do operador na coluna ao lado da placa
                        placa['Operador'] = operador
                        if operador in operadores:
                            pass
                        else:
                            operadores.append(operador)

                        px.write(str(placa['Valor']).replace('.', ','))
                        diferencas.append(diferenca)
                        placa['Diferenca'] = diferenca
                        print(f'Valor no sistema {valor_antigo} // Valor na planilha {placa['Valor']}')
                        print(f'Placa: {placa['Placa']} // Operador: {operador}')
                        qtd -= 1
                    
                    #clicar em incluir
                    px.click(474,239)
                    px.write('y')
                    sleep(0.5)
                else:
                    #pass
                    pass
                #clicar para sair
                px.click(876,212, duration=0.5)
                #--- repita até acabar o total de placas
            else:
                
                pass
        #salvar
        sleep(1)
        px.click(360,102, duration=0.5)
        sleep(5)
        #clicar esc ou enter
        px.press('enter')
        sleep(2)
        
        #próximo
        px.click(641,104, duration=0.5)
        sleep(1.5)
        px.press('enter')
        #repita o processo
        print('')
        print(f'Operador {cont}º: {operador} finalizado.')
        print(f'Com a diferença total de {sum(diferencas):.2f}')
        print('=+' * 20)
        print('')
        cont += 1
        sleep(5)
    #print(valor)
    for operator in operadores:
        print(f'Operador nº {operator}')
        diferencas_caixas = list()
        for dados in lista:
            if operator == dados['Operador']:
                try:
                    diferencas_caixas.append(dados['Diferenca'])
                except:
                    print('Não existe diferença')
                print(f'Aut: {dados['Placa']} // Valor mudado: {dados['Valor']} // Diferença total: {dados['Diferenca']}')
            
        try:
            print(f'Com a diferença total de {sum(diferencas_caixas):.2f}')
        except:
            print('Não existe diferença')
        
        print('=+' * 20)
        print('')

    contador = 0
    print('Valores não achados:')
    for dados in lista:
        if dados['Operador'] == '':
            print(f'Aut: {dados['Placa']} // Valor: {dados['Valor']}')
            contador += 1

    print(f'Qtd de autorização não achada: {contador}')
    print('=+' * 20)
    print('')


def proximo():
    sleep(1)
    px.click(641,102, duration=0.5)
    sleep(3)

