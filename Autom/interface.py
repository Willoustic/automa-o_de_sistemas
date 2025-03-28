import tkinter as tk
from .execução import executar
from .verificar import auto, rela, verificar_dados
from time import sleep

def aplicativo():
    def ajeitar_caixas_pv():
        def verdadeiro():
            valor_global.set(True)
            verificar_situação()

        def falso():
            valor_global.set(False)
            verificar_situação()

        def verificar_situação():
            if valor_global.get() == True:
                temp.destroy()
                executar(10)
                

            elif valor_global.get() == False:
                temp.destroy()

        temp = tk.Tk()
        temp.title('Confirmação')
        aviso = tk.Label(temp, text='Confirma a execução?', font='Arial, 15')
        aviso.grid(row=1, column=1)
        aviso_2 = tk.Label(temp, text='Recomendo fechar e abrir o Fechamento PDV para confirmar', font='Arial, 13')
        aviso_2.grid(row=2, column=1)
        
        valor_global = tk.BooleanVar()

        confirm = tk.Button(temp, text=' Sim ', command=verdadeiro)
        decline = tk.Button(temp, text=' Não ', command=falso)
        
        confirm.grid(row=4, column=1)
        decline.grid(row=5, column=1)

        temp.mainloop()

    def ajeitar_caixas_zn():
        
        def verdadeiro():
            valor_global.set(True)
            verificar_situação()

        def falso():
            valor_global.set(False)
            verificar_situação()

        def verificar_situação():
            if valor_global.get() == True:
                temp.destroy()
                executar(12)
                

            elif valor_global.get() == False:
                temp.destroy()

        temp = tk.Tk()
        temp.title('Confirmação')
        aviso = tk.Label(temp, text='Confirma a execução?', font='Arial, 15')
        aviso.grid(row=1, column=1)
        aviso_2 = tk.Label(temp, text='Recomendo fechar e abrir o Fechamento PDV para confirmar', font='Arial, 13')
        aviso_2.grid(row=2, column=1)
        
        valor_global = tk.BooleanVar()

        confirm = tk.Button(temp, text=' Sim ', command=verdadeiro)
        decline = tk.Button(temp, text=' Não ', command=falso)
        
        confirm.grid(row=4, column=1)
        decline.grid(row=5, column=1)



        temp.mainloop()

    def ajeitar_caixas_zs():
        def verdadeiro():
            valor_global.set(True)
            verificar_situação()

        def falso():
            valor_global.set(False)
            verificar_situação()

        def verificar_situação():
            if valor_global.get() == True:
                temp.destroy()
                executar(3)
                

            elif valor_global.get() == False:
                temp.destroy()

        temp = tk.Tk()
        temp.title('Confirmação')
        aviso = tk.Label(temp, text='Confirma a execução?', font='Arial, 15')
        aviso.grid(row=1, column=1)
        aviso_2 = tk.Label(temp, text='Recomendo fechar e abrir o Fechamento PDV para confirmar', font='Arial, 13')
        aviso_2.grid(row=2, column=1)
        
        valor_global = tk.BooleanVar()

        confirm = tk.Button(temp, text=' Sim ', command=verdadeiro)
        decline = tk.Button(temp, text=' Não ', command=falso)
        
        confirm.grid(row=4, column=1)
        decline.grid(row=5, column=1)

        temp.mainloop()   

    def verificar():
        root2.update()
        relatorio = rela()
        lista = auto(relatorio)
        temp = tk.Tk()
        temp.title('AVISO!')
        aviso = tk.Label(temp, text='Verificar no console as autorizações e valores', font='Arial, 15')
        aviso.grid(row=1, column=1)
        aviso_2 = tk.Label(temp, text='Após verificar, fechar essa janela', font='Arial, 13')
        aviso_2.grid(row=2, column=1)
        espaco_temp = tk.Label(text=' ', font='arial, 5')
        espaco_temp.grid(row=3, column=1)
        
        verificar_dados(lista)

        def fechar():
            temp.destroy()
        
        fechar()


 
    root2 = tk.Tk()
    root2.title('Automatização de Caixas')
    root2.geometry('400x290')
    espaco_0 = tk.Label(root2, text=' ', font='arial, 15')
    espaco_0.grid(row=1, column=1)
    main_text = tk.Label(root2, text='Automatização de caixas', font='Arial, 15')
    main_text.grid(row=1, column=2)
    
    espaco_0 = tk.Label(root2, text=' ', font='arial, 2')
    espaco_0.grid(row=2, column=1)

    verificar_info = tk.Label(root2, text='Verificar os dados', font='Arial, 10')
    verificar_but = tk.Button(root2, text='Verificar', command=verificar)

    verificar_info.grid(row=3, column=2)
    verificar_but.grid(row=4, column=2)
    
    text_zn = tk.Label(root2, text='Mudar Zona Norte', font='Arial, 8')
    exec_zn = tk.Button(root2, text='Zona Norte', command=ajeitar_caixas_zn)

    espaco_2 = tk.Label(root2, text=' ', font='arial, 15')
    espaco_2.grid(row=5, column=2)

    text_zn.grid(row=6, column=1)
    exec_zn.grid(row=7, column=1)

    text_pv = tk.Label(root2, text='Mudar Posto Vitória', font='Arial, 8')
    exec_pv = tk.Button(root2, text='Posto Vitória', command=ajeitar_caixas_pv)

    text_pv.grid(row=6, column=2)
    exec_pv.grid(row=7, column=2)

    text_pv = tk.Label(root2, text='Mudar Zona Sul', font='Arial, 8')
    exec_pv = tk.Button(root2, text='Zona Sul', command=ajeitar_caixas_zs)

    text_pv.grid(row=6, column=3)
    exec_pv.grid(row=7, column=3)

    def mudar_custom():
        texto_global.set('Nenhum valor digitado')
        qtd = personalizado.get()
        try:
            qtd = int(qtd)
            texto_global.set(f'Qtd de caixas a mudar autorizações: {qtd}')
        except:
            texto_global.set('Valor digitado incorretamente')
        else:
            def verdadeiro():
                valor_global.set(True)
                verificar_situação()

            def falso():
                valor_global.set(False)
                verificar_situação()

            def verificar_situação():
                if valor_global.get() == True:
                    temp.destroy()
                    executar(int(qtd))
                    
                elif valor_global.get() == False:
                    temp.destroy()

            temp = tk.Tk()
            temp.title('Confirmação')
            aviso = tk.Label(temp, text='Confirma a execução?', font='Arial, 15')
            aviso.grid(row=1, column=1)
            aviso_2 = tk.Label(temp, text='Recomendo fechar e abrir o Fechamento PDV para confirmar', font='Arial, 13')
            aviso_2.grid(row=2, column=1)
            
            valor_global = tk.BooleanVar()

            confirm = tk.Button(temp, text=' Sim ', command=verdadeiro)
            decline = tk.Button(temp, text=' Não ', command=falso)
            
            confirm.grid(row=4, column=1)
            decline.grid(row=5, column=1)

            temp.mainloop()

    espaco_3 = tk.Label(root2, text=' ', font='arial, 15')
    espaco_3.grid(row=8, column=2)

    p = tk.Label(root2, text='Personalizado', font='Arial, 14')
    p.grid(row=9, column=2)

    personalizado = tk.Entry(root2)
    personalizado.grid(row=10, column=2)
    
    custom = tk.Button(root2, text='Mudar valores', command=mudar_custom)
    custom.grid(row=11, column=2)
    
    texto_global = tk.StringVar()

    texto_info = tk.Label(root2, textvariable=texto_global)
    texto_info.grid(row=12, column=2)
    
    root2.mainloop()
