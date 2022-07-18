from Modulos import *

class Funcs():

    def cria(self):
        self.empresa = ''

    def seleciona_revenda(self):
        self.listbox_res = Listbox(self.resultado, width=113, height=35)
        self.listbox_res.place(relx=0.01, rely=0.01)
        self.btn_erro = Button(self.resultado, text = 'Imprime erros', font=('verdana', 8, 'bold'), bg = '#D3D3D3', height = 2, width = 20)
        self.btn_erro.place(relx = 0.25, rely = 0.93)
        self.btn_fim = Button(self.resultado, text = 'Imprime Validação', font=('verdana', 8, 'bold'), bg = '#D3D3D3', height = 2, width = 20,state='disable')
        self.btn_fim.place(relx = 0.55, rely = 0.93)
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
        self.leitura_banco()
        
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
        btn_validar = Button(self.frame_selecao, text='VALIDAR', font=('verdana', 13, 'bold'), bg = '#D3D3D3', height = 5, 
          width = 20, command=self.seleciona_revenda)
        btn_validar.place(relx=0.32, rely=0.3)
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

  
        
        
      
