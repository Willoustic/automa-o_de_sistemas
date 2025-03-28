import tkinter as tk
from backend import bancobd, atualizar_banco, atualizar_nomes
from time import sleep

def tela_de_login():

    def login_usuario():
        situação.set(False)
        bancodb = bancobd()
        banco_dic = atualizar_banco(bancodb.read())
        banco_nomes = atualizar_nomes(banco_dic)

        for l, k in enumerate(banco_dic):
            usuario = str(nome_usuario.get()).strip().lower().capitalize()
            senha = str(nome_senha.get()).strip().lower().capitalize()
            if usuario == str(k['Nome']).strip().lower().capitalize():
                if len(senha) < 6:
                    text_aviso.set('Senha invalida')
                    pass
                elif senha == str(k['Senha']).strip().lower().capitalize():
                    situação.set(True)
                    text_aviso.set('')
                    root.destroy()
                    break
                else:
                    break
                    
        if usuario != str(k['Nome']).strip().lower().capitalize():    
            text_aviso.set('Login incorreto')
        elif senha != str(k['Senha']).strip():
            text_aviso.set('Senha invalida')

    def cadastrar_usuario():
        temp = tk.Tk()
        temp.title('Cadastro')
        temp.geometry('200x200')
        
        def verificar():

            danger.set('')
            nome_cad = str(nome_entry.get().strip().lower().capitalize())
            senha_cad = str(senha_entry.get().strip())
            conf_cad = str(conf_entry.get().strip())
            
            bancodb = bancobd()
            banco_dic = atualizar_banco(bancodb.read())
            banco_nomes = atualizar_nomes(banco_dic)

            for nome in banco_nomes:
                if str(nome).strip().lower().capitalize() == nome_cad:
                    break

            if nome_cad == nome:
                danger.set('Usúario já cadastrado')
                #print('Usúario já cadastrado')
                temp.update()
            elif '.' in nome_cad:
                danger.set('Caractere inválido "."! ')
                temp.update()
            else:
                if len(senha_cad) >= 6:
                    if senha_cad != conf_cad:
                        danger.set('Senhas não coincidem')
                        #print('Senhas não coincidem')
                        temp.update()
                    else:
                        danger.set(f'Usúario {nome_cad} cadastrado com sucesso!')
                        bancodb.write(f'{nome_cad};{senha_cad}.\n')
                        #print(f'Usúario {nome_cad} cadastrado com sucesso!')
                        temp.update()
                        sleep(2)
                        bancodb = bancobd()
                        banco_dic = atualizar_banco(bancodb.read())
                        banco_nomes = atualizar_nomes(banco_dic)
                        temp.destroy()
                else:
                    #print('Senha menor que 6 caracteres')
                    danger.set('Senha menor que 6 caracteres')
                    temp.update()

        cad_text = tk.Label(temp, text='Cadastrar Usúario', font='Times, 15')
        cad_text.grid(row=1, column=2)
        espaco = tk.Label(temp, text='      ', font='Times, 1')
        espaco.grid(row=1, column=1)

        nome_text = tk.Label(temp, text='Nome', font='Times, 8')
        nome_text.grid(row=3, column=2)
        senha_text = tk.Label(temp, text='Senha', font='Times, 8')
        senha_text.grid(row=5, column=2)
        conf_senha_text = tk.Label(temp, text='Confirme Senha', font='Times, 8')
        conf_senha_text.grid(row=7, column=2)

        nome_entry1 = tk.StringVar()
        
        senha_entry1 = tk.StringVar()
        
        conf_entry1 = tk.StringVar()

        nome_entry = tk.Entry(temp, textvariable=nome_entry1)
        nome_entry.grid(row=4, column=2)
        senha_entry = tk.Entry(temp, textvariable=senha_entry1, show='*')
        senha_entry.grid(row=6, column=2)
        conf_entry = tk.Entry(temp, textvariable=conf_entry1, show='*')
        conf_entry.grid(row=8, column=2)

        cadastrar = tk.Button(temp, text='Cadastrar', command=verificar)
        cadastrar.grid(row=9, column=2)
        
        danger = tk.StringVar(temp)

        text_danger = tk.Label(temp, textvariable=danger, font='Times, 8')
        text_danger.grid(row=11, column=2)

        espaco3 = tk.Label(temp, text='', font='Times, 1')
        espaco3.grid(row=12, column=2)

        temp.mainloop()

    bancodb = bancobd()
    banco_dic = atualizar_banco(bancodb.read())
    banco_nomes = atualizar_nomes(banco_dic)

    if len(banco_dic) < 1:
        temp = tk.Tk()
        temp.title('Aviso')
        temp_text = tk.Label(temp, text='Nenhum usuário cadastrado!')
        temp_text.pack(pady=2)
        temp.mainloop()

    root = tk.Tk()
    root.title('Login')
    root.geometry('200x200')

    situação = tk.BooleanVar()

    espaco = tk.Label(root, text='     ', font='Times, 15')
    espaco.grid(row=1, column=1)

    login = tk.Label(root, text='Login', font='Times, 15')
    login.grid(row=1, column=2)

    nome_name = tk.Label(root, text='Usúario', anchor='w')
    nome_name.grid(row=2, column=2, )
    nome_usuario = tk.Entry()
    nome_usuario.grid(row=3, column=2)
    senha_name = tk.Label(root, text='Senha', anchor='nw')
    senha_name.grid(row=4, column=2)
    nome_senha = tk.Entry(root, show='*')
    nome_senha.grid(row=5, column=2)
    login_button = tk.Button(root, text='Login', command=login_usuario)
    login_button.grid(row=7, column=2)

    espaco2 = tk.Label(root, text='', font='Times, 1')
    espaco2.grid(row=8, column=2)

    text_aviso = tk.StringVar()
    aviso = tk.Label(root, textvariable=text_aviso, font='Arial, 8')
    aviso.grid(row=9, column=2)

    cadastro = tk.Button(root, text='Cadastrar usúario', font='Arial, 8', command=cadastrar_usuario)
    cadastro.grid(row=11, column=2)
    root.mainloop()
    
    if situação.get() == True:
        return True
    else:
        return False
