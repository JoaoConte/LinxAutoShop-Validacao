from Modulos import *

class Grava():
    def limpa_tela(self):
        self.ent_cod.delete(0, END)
        self.t_modulo.set("Selecione o modulo")
        self.ent_id.delete(0, END)
        self.ent_processo.delete(0, END)
        self.ent_tabela.delete(0, END)
        self.ent_inner1.delete(0, END)
        self.ent_inner1t.delete(0, END)
        self.ent_innerca11.delete(0, END)
        self.ent_innerco11.delete(0, END)
        self.ent_innerca12.delete(0, END)
        self.ent_innerco12.delete(0, END)
        self.ent_innerca13.delete(0, END)
        self.ent_innerco13.delete(0, END)
        self.ent_inner2.delete(0, END)
        self.ent_inner2t.delete(0, END)
        self.ent_innerca21.delete(0, END)
        self.ent_innerco21.delete(0, END)
        self.ent_innerca22.delete(0, END)
        self.ent_innerco22.delete(0, END)
        self.ent_innerca23.delete(0, END)
        self.ent_innerco23.delete(0, END)
        self.ent_where1.delete(0, END)
        self.ent_comp_w1.delete(0, END)
        self.ent_where2.delete(0, END)
        self.ent_comp_w2.delete(0, END)
        self.ent_where3.delete(0, END)
        self.ent_comp_w3.delete(0, END)
        self.ent_where4.delete(0, END)
        self.ent_comp_w4.delete(0, END)
        self.ent_where5.delete(0, END)
        self.ent_comp_w5.delete(0, END)
        self.ent_ocorr.delete(0,END)
        self.t_where1.set(self.lista_where[0])
        self.t_where2.set(self.lista_where[0])
        self.t_where3.set(self.lista_where[0])
        self.t_where4.set(self.lista_where[0])
        self.t_where5.set(self.lista_where[0])

    def var_valida(self):
        if self.t_modulo.get()[0:2] == "('":
            self.v_modulo = self.t_modulo.get()[2:len(self.t_modulo.get())-3]
        else:
            self.v_modulo = self.t_modulo.get()
        if self.v_modulo == 'Selecione o modulo':
            messagebox.showwarning(title='Preenchimento', message='Campo MODULO não pode ter preenchimento padrao')
            #self.t_modulo.focus_set()
            return
        self.v_processo = self.ent_processo.get()
        self.v_id = self.ent_id.get()
        if self.v_id == '':
            messagebox.showwarning(title='Preenchimento', message='Campo ID obrigatório')
            self.ent_id.focus_set()
            return
        if self.v_processo == '':
            messagebox.showwarning(title = 'Preenchimento', message = 'Campo PROCESSO obrigatório')
            self.ent_processo.focus_set()
            return
        self.v_tab_pri = self.ent_tabela.get()
        if self.v_tab_pri == '':
            messagebox.showwarning(title = 'Preenchimento', message = 'Campo TABELA PRINCIPAL obrigatório')
            self.ent_tabela.focus_set()
            return
        self.v_inner1 = self.ent_inner1.get()
        self.v_inner_tab1 = self.ent_inner1t.get()
        self.v_c11_lig_tab = self.ent_innerca11.get()
        self.v_c11_lig_tab_pri = self.ent_innerco11.get()
        self.v_c12_lig_tab = self.ent_innerca12.get()
        self.v_c12_lig_tab_pri = self.ent_innerco12.get()
        self.v_c13_lig_tab = self.ent_innerca13.get()
        self.v_c13_lig_tab_pri = self.ent_innerco13.get()
        self.v_inner2 = self.ent_inner2.get()
        self.v_inner_tab2 = self.ent_inner2t.get()
        self.v_c21_lig_tab = self.ent_innerca21.get()
        self.v_c21_lig_tab_pri = self.ent_innerco21.get()
        self.v_c22_lig_tab = self.ent_innerca22.get()
        self.v_c22_lig_tab_pri = self.ent_innerco22.get()
        self.v_c23_lig_tab = self.ent_innerca23.get()
        self.v_c23_lig_tab_pri = self.ent_innerco23.get()
        self.v_wc1_tab = self.ent_where1.get()
        if self.v_wc1_tab == '':
            messagebox.showwarning(title = 'Preenchimento', message = 'Campo WHERE, preenchimento obrigatório')
            self.ent_where1.focus_set()
            return
        self.v_tw1 = self.t_where1.get()
        self.v_comp_w1 = self.ent_comp_w1.get()
        self.v_wc2_tab = self.ent_where2.get()
        self.v_tw2 = self.t_where2.get()
        self.v_comp_w2 = self.ent_comp_w2.get()
        self.v_wc3_tab = self.ent_where3.get()
        self.v_tw3 = self.t_where3.get()
        self.v_comp_w3 = self.ent_comp_w3.get()
        self.v_wc4_tab = self.ent_where4.get()
        self.v_tw4 = self.t_where4.get()
        self.v_comp_w4 = self.ent_comp_w4.get()
        self.v_wc5_tab = self.ent_where5.get()
        self.v_tw5 = self.t_where5.get()
        self.v_comp_w5 = self.ent_comp_w5.get()
        self.v_nrval = self.ent_ocorr.get()

    def select_lista(self):
        self.listacli.delete(*self.listacli.get_children())
        self.conecta_voa()
        lista = self.cursor.execute(
            '''SELECT * FROM valida;''') #'''SELECT cod_seq, modulo, id, processo, tab_pri, nr_val FROM valida;'''
        for i in lista:
            self.listacli.insert("", END, values=i)
        self.desconecta_voa()

    def deleta_reg(self):
        delsn = messagebox.askyesno('Deletar', 'Confirme para apagar o registro')
        if delsn == 0:
            self.limpa_tela()
            self.select_lista()
            return
        self.conecta_voa() #Conecta_banco.py
        self.cursor_voa.execute('DELETE FROM valida WHERE cod_seq =' + self.ent_cod.get())
        self.banco_voa.commit() #Conecta_banco.py
        self.desconecta_voa() #Conecta_banco.py
        messagebox.showinfo('Apagando', 'Registro apagado com sucesso!')
        self.limpa_tela()
        self.select_lista()

    def altera_reg(self):
        self.var_valida()
        self.conecta_voa()

        self.cursor_voa.execute('''UPDATE valida SET modulo = ?, id = ?, processo = ?, tab_pri = ?, inner1 = ?, inner_tab1 = ?, c11_lig_tab = ?, 
                                c11_lig_tab_pri = ?, c12_lig_tab = ?, c12_lig_tab_pri = ?, c13_lig_tab = ?, c13_lig_tab_pri = ?, inner2 = ?, inner_tab2 = ?,
                                c21_lig_tab = ?, c21_lig_tab_pri = ?, c22_lig_tab = ?, c22_lig_tab_pri = ?, c23_lig_tab = ?, c23_lig_tab_pri = ?, wc1_tab = ?, 
                                tw1 = ?, val_comp1 = ?, wc2_tab = ?, tw2 = ?, val_comp2 = ?, wc3_tab = ?, tw3 = ?, val_comp3 = ?, wc4_tab = ?, tw4 = ?, 
                                val_comp4 =? , wc5_tab = ?, tw5 = ?, val_comp5 = ?, nr_val = ? WHERE cod_seq = ?''',
                               (self.v_modulo, self.v_id, self.v_processo, self.v_tab_pri, self.v_inner1, self.v_inner_tab1,
                                self.v_c11_lig_tab, self.v_c11_lig_tab_pri, self.v_c12_lig_tab, self.v_c12_lig_tab_pri, self.v_c13_lig_tab,
                                self.v_c13_lig_tab_pri, self.v_inner2, self.v_inner_tab2, self.v_c21_lig_tab, self.v_c21_lig_tab_pri, self.v_c22_lig_tab,
                                self.v_c22_lig_tab_pri, self.v_c23_lig_tab, self.v_c23_lig_tab_pri, self.v_wc1_tab, self.v_tw1, self.v_comp_w1,
                                self.v_wc2_tab, self.v_tw2, self.v_comp_w2, self.v_wc3_tab, self.v_tw3, self.v_comp_w3, self.v_wc4_tab, self.v_tw4,
                                self.v_comp_w4, self.v_wc5_tab, self.v_tw5, self.v_comp_w5, self.v_nrval, self.ent_cod.get()))
        self.banco_voa.commit()
        self.desconecta_voa()
        messagebox.showinfo('Alterando', 'Registro alterado com sucesso!')
        self.limpa_tela()
        self.select_lista()

    def busca_reg(self):
        self.conecta_voa()
        self.listacli.delete(*self.listacli.get_children())
        #self.ent_processo.insert(END, '%')
        processo = self.ent_processo.get()
        self.cursor_voa.execute(
            "SELECT * FROM valida WHERE processo like '%"+ processo +"%' ORDER BY processo ASC") # cod_seq, modulo, id, processo, tab_pri, nr_val
        busca = self.cursor_voa.fetchall()
        for i in busca:
            self.listacli.insert("", END, values=i)
            self.listacli.bind('<Double-1>', self.ClickDuplo)
        self.desconecta_voa()
        self.limpa_tela()


    def add_reg(self):
        self.var_valida()
        self.conecta_voa()
        self.cursor_voa.execute('''INSERT INTO valida (modulo, id, processo, tab_pri, inner1, inner_tab1, c11_lig_tab, c11_lig_tab_pri, c12_lig_tab, 
                                   c12_lig_tab_pri, c13_lig_tab, c13_lig_tab_pri, inner2, inner_tab2, c21_lig_tab, c21_lig_tab_pri, c22_lig_tab, 
                                   c22_lig_tab_pri, c23_lig_tab, c23_lig_tab_pri, wc1_tab, tw1, val_comp1, wc2_tab, tw2, val_comp2, wc3_tab, tw3,
                                   val_comp3, wc4_tab, tw4, val_comp4, wc5_tab, tw5, val_comp5, nr_val) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                                   ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                (self.v_modulo, self.v_id, self.v_processo, self.v_tab_pri, self.v_inner1, self.v_inner_tab1, self.v_c11_lig_tab,
                                 self.v_c11_lig_tab_pri, self.v_c12_lig_tab, self.v_c12_lig_tab_pri, self.v_c13_lig_tab, self.v_c13_lig_tab_pri,
                                 self.v_inner2, self.v_inner_tab2, self.v_c21_lig_tab, self.v_c21_lig_tab_pri, self.v_c22_lig_tab,
                                 self.v_c22_lig_tab_pri, self.v_c23_lig_tab, self.v_c23_lig_tab_pri, self.v_wc1_tab, self.v_tw1, self.v_comp_w1,
                                 self.v_wc2_tab, self.v_tw2, self.v_comp_w2, self.v_wc3_tab, self.v_tw3, self.v_comp_w3, self.v_wc4_tab,
                                 self.v_tw4, self.v_comp_w4, self.v_wc5_tab, self.v_tw5, self.v_comp_w5, self.v_nrval))
        self.banco_voa.commit()
        messagebox.showinfo('Inclusão', 'Registro gravado com sucesso!')
        self.desconecta_voa()
        self.select_lista()
        self.limpa_tela()

