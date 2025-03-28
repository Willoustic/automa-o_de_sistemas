import tkinter as tk
from Autom.Automação import Aut
from Fech.Fechamento import Fec

def opções():

    def autom():
        Aut()

    def fech():
        Fec()

    root = tk.Tk()
    root.title('Aplicações')
    root.geometry('400x150')

    espaco = tk.Label(root, text='       ', font='Arial, 15')
    espaco.grid(row=0 , column=0)

    title = tk.Label(root, text='Aplicações', font='Times, 15', anchor='center')
    title.grid(row=0, column=2)

    button1 = tk.Button(root, text='Por autorizações', command=autom, anchor='w')
    button2 = tk.Button(root, text='Fechamento', command=fech, anchor='w')

    button1.grid(row=2, column=1)
    button2.grid(row=2, column=3)

    espaco1 = tk.Label(root, text='', font='Arial, 15')
    espaco1.grid(row=1, column=1)

    espaco2 = tk.Label(root, text='', font='Arial, 15')
    espaco2.grid(row=1 , column=1)


    root.mainloop()
