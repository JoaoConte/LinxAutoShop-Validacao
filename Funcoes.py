from Modulos import *

class Funcs():

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
        self.lbl_emprev = Label(self.frame_selecao, text = 'Empresa/Revenda', font=('verdana', 8, 'bold'))
        self.lbl_emprev.place(relx = 0.05, rely=0.02)
        self.conecta_DB()
        self.cursor.execute("SELECT empresa, revenda,razao_social, cnpj FROM GER_REVENDA")
        self.listbox = Listbox(self.frame_selecao, width=63, height=5)
        self.listbox.place(relx=0.05, rely=0.05)
        a = 0
        for linha in self.cursor.fetchall():
            a = a + 1
            self.combo = str(linha[0]) + '.' + str(linha[1]) + ' - ' + linha[2] + ' - CNPJ: ' + linha[3][0:2]+ '.'+ linha[3][2:5] + '.'+ linha[3][5:8]+ '/'+ linha[3][8:12] + '-'+ linha[3][12:14]
            self.listbox.insert(a, self.combo)
        btn = Button(self.frame_selecao, text='Confirmar Empresa/Revenda', font=('verdana', 8, 'bold'), bg = '#D3D3D3', fg='red', command=self.seleciona_revenda)
        btn.place(relx=0.1, rely=0.2)
        self.desconecta_DB()

    def ver_versao(self):
        self.conecta_voa()
        self.cursor_voa.execute("SELECT versaodb FROM parametros")
        for linha in self.cursor_voa.fetchall():
            self.ver_db_val = linha[0]
        self.desconecta_voa()
        self.conecta_DB()
        self.cursor.execute("SELECT versao FROM ger_dbversao")
        for linha in self.cursor.fetchall():
            self.ver_db_base = linha[0]
        self.desconecta_DB() 
        if self.ver_db_base != self.ver_db_val:
            messagebox.showinfo('Versão incorreta',
                                'Versão do banco de dados da validador é ' + self.ver_db_val + '\n'
                                'e versão do banco do AutoShop é ' + self.ver_db_base + '. Para\n' 
                                'continuar, faça download da versão do banco\n'
                                'de dados do validador de acordo com a versao\n'
                                'do AutoShop')   
            exit()    
        else:
            self.frame_revenda() # Monta lista de revendas para serem selecionadas
            self.datago()        # Seleção da data de GOLIVE

  
        
        
      
