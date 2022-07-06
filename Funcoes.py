from Modulos import *

class Funcs():
    def tela_sobre(self):
        #self.telasobre = Toplevel()
        self.telasobre.title('Acesso cadastros')
        self.telasobre.geometry('200x200')
        self.telasobre.resizable(False, False)
        self.telasobre.transient(self.principal)
        self.telasobre.focus_force()
        self.telasobre.grab_set()
        self.telasobre.iconbitmap('Linx.ico')

        self.bt_ok=Button(self.telasobre, text='OK', command=self.telasobre.destroy())


    def valida_acesso(self):
        self.telasenha = Toplevel()
        self.telasenha.title('Acesso cadastros')
        self.telasenha.geometry('250x150+450+250')
        self.telasenha.resizable(False, False)
        self.telasenha.transient(self.principal)
        self.telasenha.focus_force()
        self.telasenha.grab_set()
        self.telasenha.iconbitmap('Linx.ico')

        self.lbl_usuario = Label(self.telasenha, text='Usuário')
        self.lbl_usuario.place(relx = 0.06, rely = 0.2)
        self.ent_usu = Entry(self.telasenha, relief='groove')
        self.ent_usu.place(relx=0.3, rely=0.2, width = 150)

        self.lbl_senha = Label(self.telasenha, text='Senha')
        self.lbl_senha.place(relx = 0.06, rely = 0.45)
        self.ent_senha = Entry(self.telasenha, relief='groove', show ='*')
        self.ent_senha.place(relx=0.3, rely=0.45, width = 150)

        self.btn_ok = Button(self.telasenha, text = 'OK', bg = '#D3D3D3', font=('verdana', 8 , 'bold'),height = 1, width = 10)
        self.btn_ok.place(relx = 0.10, rely=0.7)

        self.btn_cancela = Button(self.telasenha, text = 'Cancela', bg = '#D3D3D3', font=('verdana', 8 , 'bold'),height = 1, width = 10)
        self.btn_cancela.place(relx = 0.55, rely=0.7)

    def cria(self):
        self.empresa = ''

    def seleciona_revenda(self):
        empresa = []
        revenda = []
        combo_p1 = []
        cnpj = []
        for i in self.listbox.curselection():
            empresa.append(str(self.listbox.get(i)[0]))
            revenda.append(str(self.listbox.get(i)[2]))
            combo_p1.append(str(self.listbox.get(i)[0]) + '.'+str(self.listbox.get(i)[2]) + ' - ' + str(self.listbox.get(i)[6:]))
            cnpj.append(str(self.listbox.get(i)[3]))
        self.empresa = ', '.join(empresa)
        self.revenda = ', '.join(revenda)
        self.combo_p = ', '.join(combo_p1)
        self.cnpj = ', '.join(cnpj)

    def frame_revenda(self):
        self.lbl_emprev = Label(self.telaval, text = 'Empresa/Revenda', font=('verdana', 8, 'bold'))
        self.lbl_emprev.place(relx = 0.05, rely=0.02)
        self.conecta_DB()
        self.cursor.execute("SELECT empresa, revenda,razao_social, cnpj FROM GER_REVENDA")
        self.listbox = Listbox(self.telaval, width=63, height=5)
        self.listbox.place(relx=0.05, rely=0.05)
        a = 0
        for linha in self.cursor.fetchall():
            a = a + 1
            self.combo = str(linha[0]) + '.' + str(linha[1]) + ' - ' + linha[2] + ' - CNPJ: ' + linha[3][0:2]+ '.'+ linha[3][2:5] + '.'+ linha[3][5:8]+ '/'+ linha[3][8:12] + '-'+ linha[3][12:14]
            self.listbox.insert(a, self.combo)
        btn = Button(self.telaval, text='Confirmar Empresa/Revenda', font=('verdana', 8, 'bold'), bg = '#D3D3D3', fg='red', command=self.seleciona_revenda)
        btn.place(relx=0.1, rely=0.2)
        self.desconecta_DB()

    def btn_principal(self):     # Botões Tela principal
        self.btn_parametros = Button(self.principal, text='Parâmetros', bg = '#D3D3D3', font=('verdana', 30, 'bold'),height = 1, width = 10, command=self.cad_par)
        self.btn_parametros.place(relx=0.1, rely=0.15)
        ##
        self.btn_cadastros = Button(self.principal, text='Cadastros', bg = '#D3D3D3', font=('verdana', 30, 'bold'), height = 1, width = 10, command=self.tela_cadastro) #command=self.valida_acesso
        self.btn_cadastros.place(relx=0.1,rely=0.45)
        ##
        self.btn_validacao = Button(self.principal, text='Validação', bg = '#D3D3D3', font=('verdana', 30, 'bold'),height = 1, width = 10, command=self.tela_validacao)
        self.btn_validacao.place(relx=0.1, rely=0.75)

  
        
        
      
