import tkinter as tk
from .app2 import inserir_rateio
from .automação import fechamento
from .excluir_nota import excluir_sangria
from .salvar import salvar

def aplicativo2():

    def salvar_vitoria():
        salvar(10)

    def salvar_novoh():
        salvar(12)

    def salvar_transp():
        salvar(3)

    
    def fechamento_vitoria():
        print ('fechando posto vitoria')
        fechamento(10)

    def fechamento_zn():
        print ('fechando posto zn')
        fechamento(12)

    def fechamento_zs():
        print ('fechando posto zs')
        fechamento(3)

    def rateio_ZS():
        inserir_rateio(3)

    def rateio_vitoria():    
        inserir_rateio(10)

    def rateio_ZN():
        inserir_rateio(12)
    
    def excluir_recebimento_zs():
        excluir_sangria(3)

    def excluir_recebimento_zn():
        excluir_sangria(12)
    
    def excluir_recebimento_pv():
        excluir_sangria(10)

    root2 = tk.Tk()
    root2.title('Fechamento')
    root2.geometry('470x420')

    tituto1 = tk.Label(root2, text='Fechamento de caixas', font='Arial, 13')
    tituto1.grid(row=1, column=2)

    btn1 = tk.Button(root2, text='Posto Vitoria', font='Arial, 8', command=fechamento_vitoria)
    btn2 = tk.Button(root2, text='Posto Zona Norte', font='Arial, 8', command=fechamento_zn)
    btn3 = tk.Button(root2, text='Posto Zona Sul', font='Arial, 8', command=fechamento_zs)

    btn1.grid(row=2, column=1)
    btn2.grid(row=2, column=2)
    btn3.grid(row=2, column=3)

    espaco = tk.Label(root2, text=' ', font='Arial, 15')
    espaco.grid(row=3, column=2)

    tituto2 = tk.Label(root2, text='Rateio de caixas', font='Arial, 13')
    tituto2.grid(row=4, column=2)

    btn4 = tk.Button(root2, text='Posto Vitoria', font='Arial, 8', command=rateio_vitoria)
    btn5 = tk.Button(root2, text='Posto Zona Norte', font='Arial, 8', command=rateio_ZN)
    btn6 = tk.Button(root2, text='Posto Zona Sul', font='Arial, 8', command=rateio_ZS)

    btn4.grid(row=5, column=1)
    btn5.grid(row=5, column=2)
    btn6.grid(row=5, column=3)

    espaco = tk.Label(root2, text=' ', font='Arial, 15')
    espaco.grid(row=6, column=2)

    tituto1 = tk.Label(root2, text='Excluir espécies', font='Arial, 13')
    tituto1.grid(row=7, column=2)

    btn7 = tk.Button(root2, text='Posto Vitoria', font='Arial, 8', command=excluir_recebimento_pv)
    btn8 = tk.Button(root2, text='Posto Zona Norte', font='Arial, 8', command=excluir_recebimento_zn)
    btn9 = tk.Button(root2, text='Posto Zona Sul', font='Arial, 8', command=excluir_recebimento_zs)

    btn7.grid(row=8, column=1)
    btn8.grid(row=8, column=2)
    btn9.grid(row=8, column=3)

    espaco = tk.Label(root2, text=' ', font='Arial, 15')
    espaco.grid(row=9, column=2)

    tituto2 = tk.Label(root2, text='Personalizado', font='Arial, 13')
    tituto2.grid(row=10, column=2)

    subtitulo1 = tk.Label(root2, text='Quantidade de caixas abaixo', font='Arial, 8')
    subtitulo1.grid(row=11, column=1)

    subtitulo2 = tk.Label(root2, text='Quantidade de caixas abaixo', font='Arial, 8')
    subtitulo2.grid(row=11, column=3)

    subtitulo3 = tk.Label(root2, text='Quantidade de caixas abaixo', font='Arial, 8')
    subtitulo3.grid(row=11, column=2)

    def pegar_valor():
        valor = entry2.get()
        if valor.isnumeric() == False:
            print("Valor digitado não é um número.")
            print(valor)
        else:        
            print(f'Valor inserido: {valor}')
            fechamento(int(valor))
        return valor

    def rateio():
        valor = entry.get()
        if valor.isnumeric() == False:
            print("Valor digitado não é um número.")
            print(valor)
        else:        
            print(f'Valor inserido: {valor}')
            inserir_rateio(int(valor))
        return valor
    
    def especie():
        valor = entry3.get()
        if valor.isnumeric() == False:
            print("Valor digitado não é um número.")
            print(valor)
        else:        
            print(f'Valor inserido: {valor}')
            excluir_sangria(int(valor))
        return valor
    
    rateio_b = tk.Button(root2, text='Inserir Rateio', font='Arial, 8', command=rateio)
    fechamento_b = tk.Button(root2, text='Confirmar Caixas', font='Arial, 8', command=pegar_valor)
    excluir_b = tk.Button(root2, text='Excluir Especies', font='Arial, 8', command=especie)

    entry = tk.Entry(root2)
    entry.grid(row=12, column=1)
    entry3 = tk.Entry(root2)
    entry3.grid(row=12, column=2)
    entry2 = tk.Entry(root2)
    entry2.grid(row=12, column=3)

    rateio_b.grid(row=13, column=1)
    excluir_b.grid(row=13, column=2)
    fechamento_b.grid(row=13, column=3)

    espaco_1 = tk.Label(root2, text=' ', font='Arial, 15')
    espaco_1.grid(row=14, column=2)

    tituto1 = tk.Label(root2, text='Salvar caixas', font='Arial, 13')
    tituto1.grid(row=15, column=2)

    btn7 = tk.Button(root2, text='Posto Vitoria', font='Arial, 8', command=salvar_vitoria)
    btn8 = tk.Button(root2, text='Posto Zona Norte', font='Arial, 8', command=salvar_novoh)
    btn9 = tk.Button(root2, text='Posto Zona Sul', font='Arial, 8', command=salvar_transp)

    btn7.grid(row=16, column=1)
    btn8.grid(row=16, column=2)
    btn9.grid(row=16, column=3)

    espaco_2 = tk.Label(root2, text=' ', font='Arial, 15')
    espaco_2.grid(row=17, column=2)

    root2.mainloop()
