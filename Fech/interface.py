import tkinter as tk
from .automação import fechamento
from .app2 import inserir_rateio

def aplicativo():

    def pegar_valor():
        valor = entry.get()
        if valor.isnumeric() == False:
            print("Valor digitado não é um número.")
        else:        
            print(f'Valor inserido: {valor}')
            fechamento(int(valor))
        return valor

    def rateio():
        valor = entry2.get()
        if valor.isnumeric() == False:
            print("Valor digitado não é um número.")
        else:        
            print(f'Valor inserido: {valor}')
            inserir_rateio(int(valor))
        return valor
    
    root2 = tk.Tk()
    root2.title("Confirmar caixas")

    label = tk.Label(root2, text="Quantos caixas para confirmar?", font=("Times, 8"))
    label.pack(pady=1)
    entry = tk.Entry()
    entry.pack(pady=10)

    
    root2.geometry("200x200")

    botao = tk.Button(root2, text="Confirmar caixas", command=pegar_valor)
    botao.pack(pady=5)

    label2 = tk.Label(root2, text="Quantos caixas para inserir rateio?", font=("Times, 8"))
    label2.pack(pady=5)
    entry2 = tk.Entry()
    entry2.pack(pady=10)

    botao2 = tk.Button(root2, text="Inserir Rateio", command=rateio)
    botao2.pack(pady=5)


    root2.mainloop()