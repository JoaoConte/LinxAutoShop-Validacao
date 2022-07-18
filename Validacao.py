from Modulos import *

class Valida():
    #def valida_modulo(self, modulo):
    #    self.parar = 'N'
    #    self.c_modulo = modulo
    #    self.conecta_voa()
    #    self.contr_modulo = self.cursor_voa.execute("SELECT * FROM modulos WHERE codigo ='" + self.c_modulo + "'")
        #for listax in self.contr_modulo:
        #    if listax[2] == 'S':
        #        simnao = messagebox.askyesno(title='Validação ' + self.modulo, message='O ' + self.modulo + ' já foi validado, validar novamente?')
        #        print(simnao, ' ****')
        #        if simnao == 0:
        #            self.cursor_voa.execute("UPDATE modulos SET validado = 'N' WHERE codigo = '" + self.modulo + "';")
        #            self.banco_voa.commit()
        #            self.desconecta_voa()
        #        else:
        #            self.desconecta_voa()
        #            self.c_script.destroy()
        #            self.parar = 'S'
        #            return self.parar

    def leitura_banco(self):
        self.conecta_voa()
        self.contador = 0
        self.data_go = self.ent_cal.get()
        self.lista_validada = []
        self.lista_nao_validada = []
        self.conecta_DB()
        self.base = self.cursor_voa.execute("select * from valida")# where modulo = '" + self.modulo + "'")
        for linha in self.base:
            self.s_id = linha[2]
            self.s_processo = linha[3]
            self.s_tabela_pri = linha[4]
            self.s_val_minimo = linha[36]
            self.scr_valida = "SELECT COUNT(*) FROM " + self.s_tabela_pri + " rf1"
            # if linha[5] == 'N':
            #     pass
            # if linha[13] == 'N':
            #     pass
            if linha[21] != " ":
                if linha[22] == "Empresa":
                    self.scr_valida = self.scr_valida + " WHERE rf1." + linha[21] + " = " + self.empresa + " "
                if linha[22] == "Revenda":
                    self.scr_valida = self.scr_valida + " WHERE rf1." + linha[21] + " = " + self.revenda + " "
                if linha[22] == "Data":
                    if self.bancodados == 'SQLSERVER':
                        self.scr_valida = self.scr_valida + " WHERE rf1." + linha[21] + " >= " + self.data_go + " "
                    else:
                        self.scr_valida = self.scr_valida + " WHERE rf1." + linha[21] + " = TO_DATE('" + self.data_go + "', 'dd/mm/yyyy') "
                if linha[22] == "Maior que":
                    self.scr_valida = self.scr_valida + " WHERE rf1." + linha[21] + " > " + linha[23] + " "
                if linha[22] == "Menor que":
                    self.scr_valida = self.scr_valida + " WHERE rf1." + linha[21] + " < " + linha[23] + " "
                if linha[22] == "Diferente":
                    self.scr_valida = self.scr_valida + " WHERE rf1." + linha[21] + " != " + linha[23] + " "
                if linha[22] == "Igual":
                    self.scr_valida = self.scr_valida + " WHERE rf1." + linha[21] + " = " + linha[23] + " "
                if linha[22] == "IN":
                    self.scr_valida = self.scr_valida + " WHERE rf1." + linha[21] + " IN (" + linha[23] + ") "
                if linha[22] == "IS NULL":
                    self.scr_valida = self.scr_valida + " WHERE rf1." + linha[21] + " IS NULL "
                if linha[22] == "IS NOT NULL":
                    self.scr_valida = self.scr_valida + " WHERE rf1." + linha[21] + " IS NOT NULL  "
                if linha[22] == "LIKE":
                    self.scr_valida = self.scr_valida + " WHERE rf1." + linha[21] + " LIKE % " + linha[23] + " % "
### Fim bloco 1
            if linha[24] != " ":
                if linha[25] == "Empresa":
                    self.scr_valida = self.scr_valida + " AND " + linha[24] + " = " + self.empresa
                if linha[25] == "Revenda":
                     self.scr_valida = self.scr_valida + " AND " + linha[24] + " = " + self.revenda
                if linha[25] == "Data":
                    if self.bancodados == 'SQLSERVER':
                        self.scr_valida = self.scr_valida + " AND " + linha[24] + " >= " + self.data_go
                    else:
                        self.scr_valida = self.scr_valida + " AND " + linha[24] + " = TO_DATE('" + self.data_go + "', 'dd/mm/yyyy') "
                if linha[25] == "Maior que":
                    self.scr_valida = self.scr_valida + " AND " + linha[24] + " > " + linha[26]
                if linha[25] == "Menor que":
                    self.scr_valida = self.scr_valida + " AND " + linha[24] + " < " + linha[26]
                if linha[25] == "Diferente":
                    self.scr_valida = self.scr_valida + " AND " + linha[24] + " != " + linha[26]
                if linha[25] == "Igual":
                    self.scr_valida = self.scr_valida + " AND " + linha[24] + " = " + linha[26]
                if linha[25] == "IN":
                    self.scr_valida = self.scr_valida + " AND " + linha[24] + " IN (" + linha[26] + ") "
                if linha[25] == "IS NULL":
                    self.scr_valida = self.scr_valida + " AND " + linha[24] + " IS NULL  "
                if linha[25] == "IS NOT NULL":
                    self.scr_valida = self.scr_valida + " AND " + linha[24] + " IS NOT NULL  "
                if linha[25] == "LIKE":
                    self.scr_valida = self.scr_valida + "AND " + linha[24] + " LIKE %" + linha[26] + " % "
## Fim bloco 2
            if linha[27] != " ":
                if linha[28] == "Empresa":
                    self.scr_valida = self.scr_valida + " AND " + linha[27] + " = " + self.empresa
                if linha[28] == "Revenda":
                    self.scr_valida = self.scr_valida + " AND " + linha[27] + " = " + self.revenda
                if linha[28] == "Data":
                    if self.bancodados == 'SQLSERVER':
                        self.scr_valida = self.scr_valida + " AND " + linha[27] + " >= " + self.data_go
                    else:
                        self.scr_valida = self.scr_valida + " AND " + linha[27] + " = TO_DATE('" + self.data_go + "', 'dd/mm/yyyy') "
                if linha[28] == "Maior que":
                    self.scr_valida = self.scr_valida + " AND " + linha[27] + " > " + linha[29]
                if linha[28] == "Menor que":
                    self.scr_valida = self.scr_valida + " AND " + linha[27] + " < " + linha[29]
                if linha[28] == "Diferente":
                    self.scr_valida = self.scr_valida + " AND " + linha[27] + " != " + linha[29]
                if linha[28] == "Igual":
                    self.scr_valida = self.scr_valida + " AND " + linha[27] + " = " + linha[29]
                if linha[28] == "IN":
                    self.scr_valida = self.scr_valida + " AND " + linha[27] + " IN (" + linha[29] + ") "
                if linha[28] == "IS NULL":
                    self.scr_valida = self.scr_valida + " AND " + linha[27] + " IS NULL "
                if linha[28] == "IS NOT NULL":
                    self.scr_valida = self.scr_valida + " AND " + linha[27] + " IS NOT NULL "
                if linha[28] == "LIKE":
                    self.scr_valida = self.scr_valida + " AND " + linha[27] + " LIKE %" + linha[29] + " % "
## Fim bloco 3
            if linha[30] != " ":
                if linha[31] == "Empresa":
                    self.scr_valida = self.scr_valida + " AND " + linha[30] + " = " + self.empresa
                if linha[31] == "Revenda":+ " "
                if linha[31] == "Data":
                    if self.bancodados == 'SQLSERVER':
                        self.scr_valida = self.scr_valida + " AND " + linha[30] + " >= " + self.data_go
                    else:
                        self.scr_valida = self.scr_valida + " AND " + linha[30] + " = TO_DATE('" + self.data_go + "', 'dd/mm/yyyy') "
                if linha[31] == "Maior que":
                    self.scr_valida = self.scr_valida + " AND " + linha[30] + " > " + linha[32]
                if linha[31] == "Menor que":
                    self.scr_valida = self.scr_valida + " AND " + linha[30] + " < " + linha[32]
                if linha[31] == "Diferente":
                    self.scr_valida = self.scr_valida + " AND " + linha[30] + " != " + linha[32]
                if linha[31] == "Igual":
                    self.scr_valida = self.scr_valida + " AND " + linha[30] + " = " + linha[32]
                if linha[31] == "IN":
                    self.scr_valida = self.scr_valida + " AND " + linha[30] + " IN (" + linha[32]
                if linha[31] == "IS NULL":
                    self.scr_valida = self.scr_valida + " AND " + linha[30] + " IS NULL "
                if linha[31] == "IS NOT NULL":
                    self.scr_valida = self.scr_valida + " AND " + linha[30] + " IS NOT NULL "
                if linha[31] == "LIKE":
                    self.scr_valida = self.scr_valida + " AND " + linha[30] + " LIKE %" + linha[32] + " % "
## Fim bloco 4
            if linha[33] != " ":
                if linha[34] == "Empresa":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " = " + self.empresa
                if linha[34] == "Revenda":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " = " + self.revenda
                if linha[34] == "Data":
                    if self.bancodados == 'SQLSERVER':
                        self.scr_valida = self.scr_valida + " AND " + linha[33] + " >= " + self.data_go
                    else:
                        self.scr_valida = self.scr_valida + " AND " + linha[33] + " = TO_DATE('" + self.data_go + "', 'dd/mm/yyyy') "
                if linha[34] == "Maior que":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " > " + linha[35]
                if linha[34] == "Menor que":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " < " + linha[35]
                if linha[34] == "Diferente":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " != " + linha[35]
                if linha[34] == "Igual":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " = " + linha[35]
                if linha[34] == "IN":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " IN (" + linha[35] + ") "
                if linha[34] == "IS NULL":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " IS NULL "
                if linha[34] == "IS NOT NULL":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " IS NOT NULL "
                if linha[34] == "LIKE":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " LIKE %" + linha[35] + " % "
# ## Fim bloco 5
            lista_validada_1 = self.cursor.execute(self.scr_valida)
            #print(self.scr_valida)
            for detalhe in lista_validada_1:
                if detalhe[0] >= int(self.s_val_minimo):
                    self.lista_validada.append('- ' + linha[2] + '- ' + self.s_processo + ' - ' + str(detalhe[0]) + '- OK.')
                elif detalhe[0] < self.s_val_minimo:
                    self.contador +=1
                    self.lista_nao_validada.append('- ' + linha[2] + '- ' + self.s_processo + ' - registros encontrados ' + str(detalhe[0]) + ', registros necessários ' + str(self.s_val_minimo) +  ' - NÃO OK.')
                    self.listbox_res.insert(self.contador, '- ' + linha[2] + '- ' + self.s_processo + ' - registros encontrados ' + str(detalhe[0]) + ', registros necessários ' + str(self.s_val_minimo) +  ' - NÃO OK.')
        self.desconecta_DB()
        self.desconecta_voa()

        #self.conecta_DB()
        #self.conecta_voa()
        #if self.contador == 0:
        #    self.geraRel('Processo Validado em ', self.lista_validada)
        #    self.cursor_voa.execute("UPDATE modulos SET validado = 'S' WHERE codigo = '" + self.modulo + "';")
        #    self.banco_voa.commit()
        #else:
        #    self.geraRel('Processo NÃO Validado -  ', self.lista_nao_validada)
        #    self.cursor_voa.execute("UPDATE modulos SET validado = 'N' WHERE codigo = '" + self.modulo + "';")
        #    self.banco_voa.commit()
        #self.desconecta_DB()
        #self.desconecta_voa()

    def construtor(self, modulo):
        self.modulo = modulo
        # if self.parar == 'S':
        #     return
        self.c_script = Toplevel()
        self.c_script.title('Validação - ' + self.modulo)
        self.c_script.geometry('840x400+250+150')
        self.c_script.resizable(False, False)
        self.c_script.transient(self.telaval)
        self.c_script.focus_force()
        self.c_script.grab_set()
        self.c_script.iconbitmap('Linx.ico')
        if self.modulo == 'PECAS':
            self.v_politica = StringVar()
            self.v_politica.set(0)
            self.excesp1 = Checkbutton(self.c_script, text='Não validar politica de preços', variable=self.v_politica, onvalue='2.2.3', offvalue='S')
            self.excesp1.place(relx = 0.05, rely = 0.05)
            self.v_markup = StringVar()
            self.excesp2 = Checkbutton(self.c_script, text='Não validar markup', variable=self.v_markup, onvalue='N', offvalue='S')
            self.v_markup.set(0)
            self.excesp2.place(relx=0.05, rely=0.1)
            self.v_kit = StringVar()
            self.excesp3 = Checkbutton(self.c_script, text='Não validar kit de itens', variable=self.v_kit, onvalue='N', offvalue='S')
            self.v_kit.set(0)
            self.excesp3.place(relx=0.05, rely=0.15)
        if self.modulo == 'VEICULOS':
            self.v_ops_aval = StringVar()
            self.excesv1 = Checkbutton(self.c_script, text='Não validar opcionais na avaliação', variable=self.v_ops_aval, onvalue='N', offvalue='S')
            self.v_ops_aval.set(0)
            self.excesv1.place(relx = 0.05, rely = 0.05)
            self.v_opcional = StringVar()
            self.excesv2 = Checkbutton(self.c_script, text='Não validar opcionais', variable=self.v_opcional, onvalue='N', offvalue='S',)
            self.v_opcional.set(0)
            self.excesv2.place(relx=0.05, rely=0.1)
            self.v_bonus = StringVar()
            self.excesv3 = Checkbutton(self.c_script, text='Não validar bonus', variable=self.v_bonus, onvalue='N', offvalue='S')
            self.v_bonus.set(0)
            self.excesv3.place(relx=0.05, rely=0.15)
            self.v_reserva = StringVar()
            self.excesv4 = Checkbutton(self.c_script, text='Não validar reserva de veiculos', variable=self.v_reserva, onvalue='N', offvalue='S')
            self.v_reserva.set(0)
            self.excesv4.place(relx=0.05, rely=0.2)

        self.btn_validar = Button(self.c_script, text='Validar', bg = '#D3D3D3', font=('verdana', 8, 'bold'), command=self.leitura_banco)
        self.btn_validar.place(relx=0.2, rely=0.65)


