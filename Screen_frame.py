from Modulos import *
from Funcoes import *

class Screen():

    def tela(self):
        self.principal.title('Validação de Operação Assistida')  # Titulo da janela
        self.principal.geometry('840x400+250+150')  # Tamanho inicial da tela
        #self.principal.configure(bg = '#422256')  # '#48185b
        self.principal.resizable(False, False)  # Redimencionamento (default = True)
        self.principal.iconbitmap('Linx.ico')


    def ClickDuplo(self, event):
        self.limpa_tela()
        self.ckduplo = self.listacli.selection()
        for n in self.listacli.selection():
            cod_seq, modulo, id, processo, tab_pri, col, inner1, inner_tab1, c11_lig_tab, c11_lig_tab_pri, c12_lig_tab, c12_lig_tab_pri, c13_lig_tab, c13_lig_tab_pri, inner2, inner_tab2, c21_lig_tab, c21_lig_tab_pri, c22_lig_tab, c22_lig_tab_pri, c23_lig_tab, c23_lig_tab_pri, wc1_tab, tw1, val_comp1, wc2_tab, tw2, val_comp2, wc3_tab, tw3, val_comp3, wc4_tab, tw4, val_comp4, wc5_tab, tw5, val_comp5, nr_val  = self.listacli.item(n, 'values')
            self.ent_cod.insert(END, cod_seq)
            self.t_modulo.set(modulo)
            self.ent_id.insert(END, id)
            self.ent_processo.insert(END, processo)
            self.ent_tabela.insert(END, tab_pri)
            self.ent_inner1.insert(END, inner1)
            self.ent_inner1t.insert(END, inner_tab1)
            self.ent_innerca11.insert(END, c11_lig_tab)
            self.ent_innerco11.insert(END, c11_lig_tab_pri)
            self.ent_innerca12.insert(END, c12_lig_tab)
            self.ent_innerco12.insert(END, c12_lig_tab_pri)
            self.ent_innerca13.insert(END, c13_lig_tab)
            self.ent_innerco13.insert(END, c13_lig_tab_pri)
            self.ent_inner2.insert(END, inner2)
            self.ent_inner2t.insert(END, inner_tab2)
            self.ent_innerca21.insert(END, c21_lig_tab)
            self.ent_innerco21.insert(END, c21_lig_tab_pri)
            self.ent_innerca22.insert(END, c22_lig_tab)
            self.ent_innerco22.insert(END, c22_lig_tab_pri)
            self.ent_innerca23.insert(END, c23_lig_tab)
            self.ent_innerco23.insert(END, c23_lig_tab_pri)
            self.ent_where1.insert(END, wc1_tab)
            self.t_where1.set(tw1)
            self.ent_comp_w1.insert(END, val_comp1)
            self.ent_where2.insert(END, wc2_tab)
            self.t_where2.set(tw2)
            self.ent_comp_w2.insert(END, val_comp2)
            self.ent_where3.insert(END, wc3_tab)
            self.t_where3.set(tw3)
            self.ent_comp_w3.insert(END, val_comp3)
            self.ent_where4.insert(END, wc4_tab)
            self.t_where4.set(tw4)
            self.ent_comp_w4.insert(END, val_comp4)
            self.ent_where5.insert(END, wc5_tab)
            self.t_where5.set(tw5)
            self.ent_comp_w5.insert(END, val_comp5)
            self.ent_ocorr.insert(END, nr_val)

    def tela_cadastro(self):
        self.valida_campo = 0
        self.telacad = Toplevel()
        self.telacad.title('Cadastros')
        self.telacad.geometry('1350x650')
#        self.telacad.configure(bg = '#422256')
        self.telacad.resizable(False, False)
        self.telacad.transient(self.principal)
        self.telacad.iconbitmap('Linx.ico')
        self.telacad.focus_force()
        self.telacad.grab_set()
        #
        self.frame1 = Frame(self.telacad, highlightbackground="blue", highlightthickness=0.5)  # Criação dos frames
        self.frame1.place(relx=0.02, rely=0.03, relwidth=0.96, relheight=0.45)  # Posição relativa do Frame
        #
        self.btn_novo = Button(self.frame1, text='Gravar', bg = '#D3D3D3', font=('verdana', 8, 'bold'), command=self.add_reg)  # GravaTabelas.py
        self.btn_novo.place(relx=0.82, rely=0.90) # POSIÇÃO ORIGINAL 0.77
        #
        # self.btn_novo = Button(self.frame1, text='Buscar', bg = '#D3D3D3', font=('verdana', 8, 'bold'), command=self.busca_reg)  # GravaTabelas.py
        # self.btn_novo.place(relx=0.82, rely=0.90)
        # #
        self.btn_alterar = Button(self.frame1, text='Alterar', bg = '#D3D3D3', font=('verdana', 8, 'bold'), command=self.altera_reg) # GravaTabelas.py
        self.btn_alterar.place(relx=0.87, rely=0.90)
        #
        self.btn_apagar = Button(self.frame1, text='Apagar', bg = '#D3D3D3', font=('verdana', 8, 'bold'), command=self.deleta_reg) # GravaTabelas.py
        self.btn_apagar.place(relx=0.92, rely=0.90)
        # Label e caixa para texto
        self.lbl_cod = Label(self.frame1, text='Código', fg='#000000', font=('verdana', 8))
        self.lbl_cod.place(relx=0.92, rely=0.04)
        self.ent_cod = Entry(self.frame1, relief='groove')
        self.ent_cod.place(relx=0.92, rely=0.11, width = 40)
        #
        self.lbl_modulo = Label(self.frame1, text='Módulo', fg='#000000', font=('verdana', 8))
        self.lbl_modulo.place(relx=0.02, rely=0.04)
        #
        self.conecta_voa()
        self.lista_modulos = self.cursor_voa.execute("SELECT codigo FROM modulos")
        #
        self.t_modulo = StringVar()
        self.t_modulo.set("Selecione o modulo")
        self.drop_modulo = OptionMenu(self.frame1, self.t_modulo, *self.lista_modulos)
        self.drop_modulo.place(relx = 0.02, rely = 0.09)
        self.desconecta_voa()
        #
        self.lbl_id = Label(self.frame1, text='ID', fg='#000000', font=('verdana', 8))
        self.lbl_id.place(relx=0.18, rely=0.04)
        self.ent_id = Entry(self.frame1, relief='groove')
        self.ent_id.place(relx=0.18, rely=0.11, width = 40)
        #
        self.lbl_processo = Label(self.frame1, text='Processo', fg='#000000', font=('verdana', 8))
        self.lbl_processo.place(relx=0.25, rely=0.04)
        self.ent_processo = Entry(self.frame1, relief='groove')
        self.ent_processo.place(relx=0.25, rely=0.11, width = 350)
        #
        self.lbl_ocorr = Label(self.frame1, text='Minimo de ocorrências',fg='#000000', font=('verdana', 8))
        self.lbl_ocorr.place(relx=0.60, rely=0.04)
        self.ent_ocorr = Entry(self.frame1, relief='groove')
        self.ent_ocorr.place(relx=0.60, rely=0.11, width = 45)
        #
        self.lbl_tabela = Label(self.frame1, text='Tabela Principal',fg='#000000', font=('verdana', 8))
        self.lbl_tabela.place(relx=0.75, rely=0.04)
        self.ent_tabela = Entry(self.frame1, relief='groove')
        self.ent_tabela.place(relx=0.75, rely=0.11, width = 150)
        #
        self.lbl_inner1 = Label(self.frame1, text='INNER 1?', fg='#107db2', font=('verdana', 8))
        self.lbl_inner1.place(relx=0.02, rely=0.20)
        self.ent_inner1 = Entry(self.frame1, relief='groove')
        self.ent_inner1.insert(0,"N")
        self.ent_inner1.place(relx=0.04, rely=0.27, width=12)
        #
        self.lbl_inner1t = Label(self.frame1, text='INNER TABELA', fg='#107db2', font=('verdana', 8))
        self.lbl_inner1t.place(relx=0.07, rely=0.20)
        self.ent_inner1t = Entry(self.frame1, relief='groove')
        self.ent_inner1t.place(relx=0.07, rely=0.27, width=150)
        #
        self.lbl_innerca11 = Label(self.frame1, text='Campo tabela (1)', fg='#107db2', font=('verdana', 8))
        self.lbl_innerca11.place(relx=0.20, rely=0.20)
        self.ent_innerca11 = Entry(self.frame1, relief='groove')
        self.ent_innerca11.place(relx=0.20, rely=0.27, width=150)
        #
        self.lbl_innerco11 = Label(self.frame1, text='Comp. tabela (1)', fg='#107db2', font=('verdana', 8))
        self.lbl_innerco11.place(relx=0.33, rely=0.20)
        self.ent_innerco11 = Entry(self.frame1, relief='groove')
        self.ent_innerco11.place(relx=0.33, rely=0.27, width=150)
        #
        self.lbl_innerca12 = Label(self.frame1, text='Campo tabela (2)', fg='#107db2', font=('verdana', 8))
        self.lbl_innerca12.place(relx=0.46, rely=0.20)
        self.ent_innerca12 = Entry(self.frame1, relief='groove')
        self.ent_innerca12.place(relx=0.46, rely=0.27, width=150)
        #
        self.lbl_innerco12 = Label(self.frame1, text='Comp. tabela (2)', fg='#107db2', font=('verdana', 8))
        self.lbl_innerco12.place(relx=0.59, rely=0.20)
        self.ent_innerco12 = Entry(self.frame1, relief='groove')
        self.ent_innerco12.place(relx=0.59, rely=0.27, width=150)
        #
        self.lbl_innerca13 = Label(self.frame1, text='Campo tabela (3)', fg='#107db2', font=('verdana', 8))
        self.lbl_innerca13.place(relx=0.72, rely=0.20)
        self.ent_innerca13 = Entry(self.frame1, relief='groove')
        self.ent_innerca13.place(relx=0.72, rely=0.27, width=150)
        #
        self.lbl_innerco13 = Label(self.frame1, text='Comp. tabela (3)', fg='#107db2', font=('verdana', 8))
        self.lbl_innerco13.place(relx=0.85, rely=0.20)
        self.ent_innerco13 = Entry(self.frame1, relief='groove')
        self.ent_innerco13.place(relx=0.85, rely=0.27, width=150)
        #
        self.lbl_inner2 = Label(self.frame1, text='INNER 2?', fg='#107db2', font=('verdana', 8))
        self.lbl_inner2.place(relx=0.02, rely=0.34)
        self.ent_inner2 = Entry(self.frame1, relief='groove')
        self.ent_inner2.insert(0,"N")
        self.ent_inner2.place(relx=0.04, rely=0.41, width=12)
        #
        self.lbl_inner2t = Label(self.frame1, text='INNER TABELA', fg='#107db2', font=('verdana', 8))
        self.lbl_inner2t.place(relx=0.07, rely=0.34)
        self.ent_inner2t = Entry(self.frame1, relief='groove')
        self.ent_inner2t.place(relx=0.07, rely=0.41, width=150)
        #
        self.lbl_innerca21 = Label(self.frame1, text='Campo tabela (1)', fg='#107db2', font=('verdana', 8))
        self.lbl_innerca21.place(relx=0.20, rely=0.34)
        self.ent_innerca21 = Entry(self.frame1, relief='groove')
        self.ent_innerca21.place(relx=0.20, rely=0.41, width=150)
        #
        self.lbl_innerco21 = Label(self.frame1, text='Comp. tabela (1)', fg='#107db2', font=('verdana', 8))
        self.lbl_innerco21.place(relx=0.33, rely=0.34)
        self.ent_innerco21 = Entry(self.frame1, relief='groove')
        self.ent_innerco21.place(relx=0.33, rely=0.41, width=150)
        #
        self.lbl_innerca22 = Label(self.frame1, text='Campo tabela (2)', fg='#107db2', font=('verdana', 8))
        self.lbl_innerca22.place(relx=0.46, rely=0.34)
        self.ent_innerca22 = Entry(self.frame1, relief='groove')
        self.ent_innerca22.place(relx=0.46, rely=0.41, width=150)
        #
        self.lbl_innerco22 = Label(self.frame1, text='Comp. tabela (2)', fg='#107db2', font=('verdana', 8))
        self.lbl_innerco22.place(relx=0.59, rely=0.34)
        self.ent_innerco22 = Entry(self.frame1, relief='groove')
        self.ent_innerco22.place(relx=0.59, rely=0.41, width=150)
        #
        self.lbl_innerca23 = Label(self.frame1, text='Campo tabela (3)', fg='#107db2', font=('verdana', 8))
        self.lbl_innerca23.place(relx=0.72, rely=0.34)
        self.ent_innerca23 = Entry(self.frame1, relief='groove')
        self.ent_innerca23.place(relx=0.72, rely=0.41, width=150)
        #
        self.lbl_innerco23 = Label(self.frame1, text='Comp. tabela (3)', fg='#107db2', font=('verdana', 8))
        self.lbl_innerco23.place(relx=0.85, rely=0.34)
        self.ent_innerco23 = Entry(self.frame1, relief='groove')
        self.ent_innerco23.place(relx=0.85, rely=0.41, width=150)
        #
        self.lbl_where1 = Label(self.frame1, text='Where campo 1', fg='#000000', font=('verdana', 8))
        self.lbl_where1.place(relx=0.02, rely=0.48)
        self.ent_where1 = Entry(self.frame1, relief='groove')
        self.ent_where1.place(relx=0.02, rely=0.55, width=150)
        #
        self.lista_where = ["Selecione", "Empresa", "Revenda", "Data", "Maior que", "Menor que", "Diferente", "Igual", "IN", "IS NULL", "IS NOT NULL", "LIKE" ]
        self.t_where1 = StringVar()
        self.t_where1.set(self.lista_where[0])
        self.drop_where1 = OptionMenu(self.frame1, self.t_where1, *self.lista_where)
        self.drop_where1.place(relx = 0.14, rely = 0.53)
        #
        self.lbl_comp_w1 = Label(self.frame1, text='Comparar Where 1', fg='#000000', font=('verdana', 8))
        self.lbl_comp_w1.place(relx=0.23, rely=0.48)
        self.ent_comp_w1 = Entry(self.frame1, relief='groove')
        self.ent_comp_w1.place(relx=0.23, rely=0.55, width=150)
        #
        self.lbl_where2 = Label(self.frame1, text='Where campo 2', fg='#107db2', font=('verdana', 8))
        self.lbl_where2.place(relx=0.02, rely=0.65)
        self.ent_where2 = Entry(self.frame1, relief='groove')
        self.ent_where2.place(relx=0.02, rely=0.72, width=150)
        #
        self.t_where2 = StringVar()
        self.t_where2.set(self.lista_where[0])
        self.drop_where2 = OptionMenu(self.frame1, self.t_where2, *self.lista_where)
        self.drop_where2.place(relx = 0.14, rely = 0.70)
        #
        self.lbl_comp_w2 = Label(self.frame1, text='Comparar Where 2', fg='#107db2', font=('verdana', 8))
        self.lbl_comp_w2.place(relx=0.23, rely=0.65)
        self.ent_comp_w2 = Entry(self.frame1, relief='groove')
        self.ent_comp_w2.place(relx=0.23, rely=0.72, width=150)
        #
        self.lbl_where3 = Label(self.frame1, text='Where campo 3', fg='#107db2', font=('verdana', 8))
        self.lbl_where3.place(relx=0.02, rely=0.81)
        self.ent_where3 = Entry(self.frame1, relief='groove')
        self.ent_where3.place(relx=0.02, rely=0.89, width=150)
        #
        self.t_where3 = StringVar()
        self.t_where3.set(self.lista_where[0])
        self.drop_where3 = OptionMenu(self.frame1, self.t_where3, *self.lista_where)
        self.drop_where3.place(relx = 0.14, rely = 0.87)
        #
        self.lbl_comp_w3 = Label(self.frame1, text='Comparar Where 3', fg='#107db2', font=('verdana', 8))
        self.lbl_comp_w3.place(relx=0.23, rely=0.81)
        self.ent_comp_w3 = Entry(self.frame1, relief='groove')
        self.ent_comp_w3.place(relx=0.23, rely=0.89, width=150)
        #
        self.lbl_where4 = Label(self.frame1, text='Where campo 4', fg='#107db2', font=('verdana', 8))
        self.lbl_where4.place(relx=0.40, rely=0.48)
        self.ent_where4 = Entry(self.frame1, relief='groove')
        self.ent_where4.place(relx=0.40, rely=0.55, width=150)
        #
        self.t_where4 = StringVar()
        self.t_where4.set(self.lista_where[0])
        self.drop_where4 = OptionMenu(self.frame1, self.t_where4, *self.lista_where)
        self.drop_where4.place(relx = 0.52, rely = 0.53)
        #
        self.lbl_comp_w4 = Label(self.frame1, text='Comparar Where 4', fg='#107db2', font=('verdana', 8))
        self.lbl_comp_w4.place(relx=0.61, rely=0.48)
        self.ent_comp_w4 = Entry(self.frame1, relief='groove')
        self.ent_comp_w4.place(relx=0.61, rely=0.55, width=150)
        #
        self.lbl_where5 = Label(self.frame1, text='Where campo 5', fg='#107db2', font=('verdana', 8))
        self.lbl_where5.place(relx=0.40, rely=0.65)
        self.ent_where5 = Entry(self.frame1, relief='groove')
        self.ent_where5.place(relx=0.40, rely=0.72, width=150)
        #
        self.t_where5 = StringVar()
        self.t_where5.set(self.lista_where[0])
        self.drop_where5 = OptionMenu(self.frame1, self.t_where5, *self.lista_where)
        self.drop_where5.place(relx=0.52, rely=0.70)
        #
        self.lbl_comp_w5 = Label(self.frame1, text='Comparar Where 5', fg='#107db2', font=('verdana', 8))
        self.lbl_comp_w5.place(relx=0.61, rely=0.65)
        self.ent_comp_w5 = Entry(self.frame1, relief='groove')
        self.ent_comp_w5.place(relx=0.61, rely=0.72, width=150)

    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.frame2 = Frame(self.telacad, highlightbackground="blue", highlightthickness=0.5)
        self.frame2.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.45)
        # DBGRID
        self.listacli = ttk.Treeview(self.frame2, columns=('COD_SEQ', 'MODULO', 'ID', 'PROCESSO', 'TAB_PRI', 'INNER1', 'INNER_TAB1',
                                                           'C11_LIG_TAB', 'C11_LIG_TAB_PRI', 'C12_LIG_TAB', 'C12_LIG_TAB_PRI',
                                                           'C13_LIG_TAB', 'C13_LIG_TAB_PRI', 'INNER2', 'INNER_TAB2', 'C21_LIG_TAB',
                                                           'C21_LIG_TAB_PRI', 'C22_LIG_TAB', 'C22_LIG_TAB_PRI', 'C23_LIG_TAB',
                                                           'C23_LIG_TAB_PRI', 'WC1_TAB', 'TW1', 'VAL_COMP1', 'WC2_TAB', 'TW2', 'VAL_COMP2',
                                                           'WC3_TAB', 'TW3', 'VAL_COMP3', 'WC4_TAB', 'TW4', 'VAL_COMP4', 'WC5_TAB', 'TW5',
                                                           'VAL_COMP5', 'NR_VAL'), show='headings')
        self.listacli.heading('COD_SEQ', text='Código')
        self.listacli.heading('MODULO', text='Módulo')
        self.listacli.heading('ID', text='ID')
        self.listacli.heading('PROCESSO', text='Processo')
        self.listacli.heading('TAB_PRI', text='Tabela Principal')
        self.listacli.heading('INNER1', text='Inner 1')
        self.listacli.heading('INNER_TAB1', text='Tab Inner 1')
        self.listacli.heading('C11_LIG_TAB', text='1 LIG')
        self.listacli.heading('C11_LIG_TAB_PRI', text='1 LIG PRINC')
        self.listacli.heading('C12_LIG_TAB', text='2 LIG')
        self.listacli.heading('C12_LIG_TAB_PRI', text='2 LIG PRINC')
        self.listacli.heading('C13_LIG_TAB', text='3 LIG')
        self.listacli.heading('C13_LIG_TAB_PRI', text='3 LIG PRINC')
        self.listacli.heading('INNER2', text='Inner 2')
        self.listacli.heading('INNER_TAB2', text='Tab Inner 2')
        self.listacli.heading('C21_LIG_TAB', text='1 LIG')
        self.listacli.heading('C21_LIG_TAB_PRI', text='1 LIG PRINC')
        self.listacli.heading('C22_LIG_TAB', text='2 LIG')
        self.listacli.heading('C22_LIG_TAB_PRI', text='2 LIG PRINC')
        self.listacli.heading('C23_LIG_TAB', text='3 LIG')
        self.listacli.heading('C23_LIG_TAB_PRI', text='3 LIG PRINC')
        self.listacli.heading('WC1_TAB', text='CAMPO WHERE 1')
        self.listacli.heading('TW1', text='TIPO WHERE 1')
        self.listacli.heading('VAL_COMP1', text='V. COMPP 1')
        self.listacli.heading('WC2_TAB', text='CAMPO WHERE 2')
        self.listacli.heading('TW2', text='TIPO WHERE 2')
        self.listacli.heading('VAL_COMP2', text='V. COMPP 2')
        self.listacli.heading('WC3_TAB', text='CAMPO WHERE 3')
        self.listacli.heading('TW3', text='TIPO WHERE 3')
        self.listacli.heading('VAL_COMP3', text='V. COMPP 3')
        self.listacli.heading('WC4_TAB', text='CAMPO WHERE 4')
        self.listacli.heading('TW4', text='TIPO WHERE 4')
        self.listacli.heading('VAL_COMP4', text='V. COMPP 4')
        self.listacli.heading('WC5_TAB', text='CAMPO WHERE 5')
        self.listacli.heading('TW5', text='TIPO WHERE 5')
        self.listacli.heading('VAL_COMP5', text='V. COMPP 5')
        self.listacli.heading('NR_VAL', text='NR.OCORR')
        self.listacli.column('COD_SEQ', minwidth = 0, width=60)
        self.listacli.column('MODULO', minwidth = 0, width=200)
        self.listacli.column('ID', minwidth = 0, width=50)
        self.listacli.column('PROCESSO', minwidth = 0, width=600)
        self.listacli.column('TAB_PRI', minwidth = 0, width=200)
        self.listacli.column('INNER1', minwidth = 0, width=0)
        self.listacli.column('INNER_TAB1', minwidth = 0, width=0)
        self.listacli.column('C11_LIG_TAB', minwidth = 0, width=0)
        self.listacli.column('C11_LIG_TAB_PRI', minwidth = 0, width=0)
        self.listacli.column('C12_LIG_TAB', minwidth = 0, width=0)
        self.listacli.column('C12_LIG_TAB_PRI', minwidth = 0, width=0)
        self.listacli.column('C13_LIG_TAB', minwidth = 0, width=0)
        self.listacli.column('C13_LIG_TAB_PRI', minwidth = 0, width=0)
        self.listacli.column('INNER2', minwidth=0, width=0)
        self.listacli.column('INNER_TAB2', minwidth=0, width=0)
        self.listacli.column('C21_LIG_TAB', minwidth = 0, width=0)
        self.listacli.column('C21_LIG_TAB_PRI', minwidth = 0, width=0)
        self.listacli.column('C22_LIG_TAB', minwidth = 0, width=0)
        self.listacli.column('C22_LIG_TAB_PRI', minwidth = 0, width=0)
        self.listacli.column('C23_LIG_TAB', minwidth = 0, width=5)
        self.listacli.column('C23_LIG_TAB_PRI', minwidth = 0, width=0)
        self.listacli.column('WC1_TAB', minwidth = 0, width=0)
        self.listacli.column('TW1', minwidth = 0, width=0)
        self.listacli.column('VAL_COMP1', minwidth = 0, width = 0)
        self.listacli.column('WC2_TAB', minwidth = 0, width = 0)
        self.listacli.column('TW2', minwidth = 0, width = 0)
        self.listacli.column('VAL_COMP2', minwidth = 0, width = 0)
        self.listacli.column('WC3_TAB', minwidth = 0, width = 0)
        self.listacli.column('TW3', minwidth = 0, width = 0)
        self.listacli.column('VAL_COMP3', minwidth = 0, width = 0)
        self.listacli.column('WC4_TAB', minwidth = 0, width = 0)
        self.listacli.column('TW4', minwidth = 0, width = 0)
        self.listacli.column('VAL_COMP4', minwidth = 0, width = 0)
        self.listacli.column('WC5_TAB', minwidth = 0, width = 0)
        self.listacli.column('TW5', minwidth = 0, width = 0)
        self.listacli.column('VAL_COMP5', minwidth = 0, width = 0)
        self.listacli.column('NR_VAL', minwidth = 0, width = 0)
        self.listacli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        self.scr1_lista = Scrollbar(self.frame2, orient='vertical')
        self.listacli.configure(yscroll=self.scr1_lista.set)
        self.scr1_lista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)
        self.scr2_lista = Scrollbar(self.frame2, orient='horizontal')
        self.listacli.configure(yscroll=self.scr2_lista.set)
        self.scr2_lista.place(relx=0.02, rely=0.96, relwidth=0.9, relheight=0.03)
        self.listacli.bind('<Double-1>', self.ClickDuplo)
        self.select_lista() # Monta grade

    def select_lista(self):
        self.listacli.delete(*self.listacli.get_children())
        self.conecta_voa()
        lista = self.cursor_voa.execute('''SELECT cod_seq, modulo, id, processo, tab_pri, nr_val,inner1, inner_tab1, c11_lig_tab,
                                        c11_lig_tab_pri, c12_lig_tab, c12_lig_tab_pri, c13_lig_tab, c13_lig_tab_pri, inner2,
                                        inner_tab2, c21_lig_tab, c21_lig_tab_pri, c22_lig_tab, c22_lig_tab_pri, c23_lig_tab,
                                        c23_lig_tab_pri, wc1_tab, tw1, val_comp1, wc2_tab, tw2, val_comp2, wc3_tab, tw3,
                                        val_comp3, wc4_tab, tw4, val_comp4, wc5_tab, tw5, val_comp5, nr_val FROM valida 
                                        ORDER BY modulo ASC;''')
        for i in lista:
            self.listacli.insert("", END, values=i)
        self.desconecta_voa()
#######***********************************************************************************************************************
    def lin_col(self):
        if self.contal == 6:
            self.lin = 0.30
        if self.contal >=6:
            self.col = 0.5
            self.lin = self.lin + 0.10
        else:
            self.lin = self.lin + 0.10

    def tela_validacao(self):
        self.conecta_voa()
        controla = self.cursor_voa.execute('''SELECT count(*) FROM modulos WHERE validado = 'S';''')
        for ver_valida in controla:
            if ver_valida[0] != 0:
                simnao = messagebox.askyesno(title='Validar novamente', message='Já foi iniciado o processo de validação, zerar?')
                if simnao == 1:
                    self.cursor_voa.execute('''UPDATE modulos SET validado = 'N' WHERE validado = 'S';''')
                    self.banco_voa.commit()

        self.ativos = self.cursor_voa.execute("SELECT count(*) FROM modulos WHERE ativo = 'S'")
        for conta_ativos in self.ativos:
            self.contav = conta_ativos[0]
        self.btv_financeiro = 'N'
        self.btv_crm = 'N'
        self.btv_mobile = 'N'
        self.btv_contabilidade = 'N'
        self.btv_oficina = 'N'
        self.btv_veiculos = 'N'
        self.btv_diversos = 'N'
        self.btv_pecas = 'N'
        self.btv_fiscal = 'N'

        self.ativa_botoes = self.cursor_voa.execute("SELECT * FROM modulos WHERE ativo = 'S'")
        for linhav in self.ativa_botoes:
            if (linhav[0] == 'CONTABILIDADE') and (linhav[1] == 'S'):
                self.btv_contabilidade = 'S'
            if (linhav[0] == 'CRM') and (linhav[1] == 'S'):
                self.btv_crm = 'S'
            if (linhav[0] == 'DIVERSOS') and (linhav[1] == 'S'):
                self.btv_diversos = 'S'
            if (linhav[0] == 'FINANCEIRO') and (linhav[1] == 'S'):
                self.btv_financeiro = 'S'
            if (linhav[0] == 'OFICINA') and (linhav[1] == 'S'):
                self.btv_oficina = 'S'
            if (linhav[0] == 'PECAS') and (linhav[1] == 'S'):
                self.btv_pecas = 'S'
            if (linhav[0] == 'VEICULOS') and (linhav[1] == 'S'):
                self.btv_veiculos = 'S'
            if (linhav[0] == 'MOBILE-DMS') and (linhav[1] == 'S'):
                self.btv_mobile = 'S'
            if (linhav[0] == 'FISCAL') and (linhav[1] == 'S'):
                self.btv_fiscal = 'S'

        self.desconecta_voa()
        self.telaval = Toplevel(self.principal)
        self.telaval.title('Validação')
        self.telaval.geometry('700x650+300+20')
        self.telaval.resizable(False, False)
        self.telaval.transient(self.principal)
        self.telaval.focus_force()
        self.telaval.grab_set()
        self.telaval.iconbitmap('Linx.ico')
        self.frame_revenda()
        #-----------------------------------------------------------------------
        self.lbl_cal = Label(self.telaval, text = 'Data GO-LIVE', font = ('verdana', 8, 'bold'))
        self.lbl_cal.place(relx = 0.63, rely = 0.02)
        self.ent_cal = DateEntry(self.telaval, locale='pt_br')
        self.ent_cal.delete(0,END)
        self.ent_cal.place(relx=0.63, rely=0.05)

        # CRM Plus
        self.contal = 1
        self.col = 0.20
        self.lin = 0.40

        while (self.contal <= self.contav):
            if self.btv_crm == 'S':
                self.btn_crm = Button(self.telaval, text='CRM PLUS', bg = '#D3D3D3', font=('verdana', 10, 'bold'), height = 3, width = 20, command=lambda:self.construtor('CRM PLUS'))
                self.btn_crm.place(relx=self.col, rely=self.lin)
                self.contal +=1
                self.lin_col()
            if self.btv_contabilidade == 'S':
                self.btn_contabil = Button(self.telaval, text='Contabilidade', bg = '#D3D3D3', font=('verdana', 10, 'bold'), height = 3, width = 20, command=lambda:self.construtor('CONTABILIDADE'))
                self.btn_contabil.place(relx=self.col, rely=self.lin)
                self.contal +=1
                self.lin_col()
            if self.btv_financeiro == 'S':
                self.btn_financ = Button(self.telaval, text='Financeiro', bg = '#D3D3D3', font=('verdana', 10, 'bold'), height = 3, width = 20, command=lambda:self.construtor('FINANCEIRO'))
                self.btn_financ.place(relx=self.col, rely=self.lin)
                self.contal +=1
                self.lin_col()
            if self.btv_oficina == 'S':
                self.btn_oficina = Button(self.telaval, text='Oficina', bg = '#D3D3D3', font=('verdana', 10, 'bold'), height = 3, width = 20, command=lambda:self.construtor('OFICINA'))
                self.btn_oficina.place(relx=self.col, rely=self.lin)
                self.contal += 1
                self.lin_col()
            if self.btv_pecas == 'S':
                self.btn_pecas = Button(self.telaval, text='Pecas', bg = '#D3D3D3', font=('verdana', 10, 'bold'), height = 3, width = 20, command=lambda:self.construtor('PECAS'))
                self.btn_pecas.place(relx=self.col, rely=self.lin)
                self.contal += 1
                self.lin_col()
            if self.btv_veiculos == 'S':
                self.btn_veiculos = Button(self.telaval, text='Veiculos', bg = '#D3D3D3', font=('verdana', 10, 'bold'), height = 3, width = 20, command=lambda:self.construtor('VEICULOS'))
                self.btn_veiculos.place(relx=self.col, rely=self.lin)
                self.contal += 1
                self.lin_col()
            if self.btv_diversos == 'S':
                self.btn_diversos = Button(self.telaval, text='Produtos Diversos', bg = '#D3D3D3', font=('verdana', 10, 'bold'), height = 3, width = 20, command=lambda:self.construtor('DIVERSOS'))
                self.btn_diversos.place(relx=self.col, rely=self.lin)
                self.contal +=1
                self.lin_col()
            if self.btv_mobile == 'S':
                self.btn_mobile = Button(self.telaval, text='Mobile DMS', bg = '#D3D3D3', font=('verdana', 10, 'bold'), height = 3, width = 20, command=lambda:self.construtor('MOBILE-DMS'))
                self.btn_mobile.place(relx=self.col, rely=self.lin)
                self.contal += 1
                self.lin_col()
            if self.btv_fiscal == 'S':
                self.btn_fiscal = Button(self.telaval, text='Fiscal', bg = '#D3D3D3', font=('verdana', 10, 'bold'), height=3, width=20, command=lambda: self.construtor('FISCAL'))
                self.btn_fiscal.place(relx=self.col, rely=self.lin)
                self.contal += 1
                self.lin_col()