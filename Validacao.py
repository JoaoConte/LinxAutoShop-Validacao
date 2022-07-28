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
            if linha[5] != 'N':
                if linha[6] != ' ':
                    self.scr_valida = self.scr_valida + " LEFT JOIN " + linha[6] + " rf2 ON rf2." + linha[7] + " = rf1." + linha[8] 
                    if linha[9] != ' ':
                        self.scr_valida = self.scr_valida + " AND rf2."+ linha[9] + " = rf1." + linha[10]
                        if linha[11] != ' ':
                            self.scr_valida = self.scr_valida + " AND rf2."+ linha[11] + " = rf1." + linha[12]
            if linha[13] != 'N':
                if linha[14] != ' ':
                    self.scr_valida = self.scr_valida + " LEFT JOIN " + linha[14] + " rf3 ON rf3." + linha[25] + " = rf1." + linha[16] 
                    if linha[17] != ' ':
                        self.scr_valida = self.scr_valida + " AND rf3."+ linha[17] + " = rf1." + linha[18]
                        if linha[19] != ' ':
                            self.scr_valida = self.scr_valida + " AND rf3."+ linha[19] + " = rf1." + linha[20]                
            if linha[21] != " ":
                if linha[23] == "Empresa":
                    self.scr_valida = self.scr_valida + " WHERE " + linha[21] + " = " + self.empresa + " "
                if linha[23] == "Revenda":
                    self.scr_valida = self.scr_valida + " WHERE " + linha[21] + " = " + self.revenda + " "
                if linha[23] == "Data":
                    if self.bancodados == 'SQLSERVER':
                        self.scr_valida = self.scr_valida + " WHERE " + linha[21] + " >= " + self.data_go + " "
                    else:
                        self.scr_valida = self.scr_valida + " WHERE " + linha[21] + " = TO_DATE('" + self.data_go + "', 'dd/mm/yyyy') "
                if linha[23] == "Maior que":
                    self.scr_valida = self.scr_valida + " WHERE " + linha[21] + " > " + linha[24] + " "
                if linha[23] == "Menor que":
                    self.scr_valida = self.scr_valida + " WHERE " + linha[21] + " < " + linha[24] + " "
                if linha[23] == "Diferente":
                    self.scr_valida = self.scr_valida + " WHERE " + linha[21] + " != " + linha[24] + " "
                if linha[23] == "Igual":
                    self.scr_valida = self.scr_valida + " WHERE " + linha[21] + " = " + linha[24] + " "
                if linha[23] == "IN":
                    self.scr_valida = self.scr_valida + " WHERE " + linha[21] + " IN (" + linha[24] + ") "
                if linha[23] == "IS NULL":
                    self.scr_valida = self.scr_valida + " WHERE " + linha[21] + " IS NULL "
                if linha[23] == "IS NOT NULL":
                    self.scr_valida = self.scr_valida + " WHERE " + linha[21] + " IS NOT NULL  "
                if linha[23] == "LIKE":
                    self.scr_valida = self.scr_valida + " WHERE " + linha[21] + " LIKE % " + linha[24] + " % "
### Fim bloco 1
            if linha[25] != " ":
                if linha[27] == "Empresa":
                    self.scr_valida = self.scr_valida + " AND " + linha[25] + " = " + self.empresa
                if linha[27] == "Revenda":
                     self.scr_valida = self.scr_valida + " AND " + linha[25] + " = " + self.revenda
                if linha[27] == "Data":
                    if self.bancodados == 'SQLSERVER':
                        self.scr_valida = self.scr_valida + " AND " + linha[25] + " >= " + self.data_go
                    else:
                        self.scr_valida = self.scr_valida + " AND " + linha[25] + " = TO_DATE('" + self.data_go + "', 'dd/mm/yyyy') "
                if linha[27] == "Maior que":
                    self.scr_valida = self.scr_valida + " AND " + linha[25] + " > " + linha[28]
                if linha[27] == "Menor que":
                    self.scr_valida = self.scr_valida + " AND " + linha[25] + " < " + linha[28]
                if linha[27] == "Diferente":
                    self.scr_valida = self.scr_valida + " AND " + linha[25] + " != " + linha[28]
                if linha[27] == "Igual":
                    self.scr_valida = self.scr_valida + " AND " + linha[25] + " = " + linha[28]
                if linha[27] == "IN":
                    self.scr_valida = self.scr_valida + " AND " + linha[25] + " IN (" + linha[28] + ") "
                if linha[27] == "IS NULL":
                    self.scr_valida = self.scr_valida + " AND " + linha[25] + " IS NULL  "
                if linha[27] == "IS NOT NULL":
                    self.scr_valida = self.scr_valida + " AND " + linha[25] + " IS NOT NULL  "
                if linha[27] == "LIKE":
                    self.scr_valida = self.scr_valida + "AND " + linha[25] + " LIKE %" + linha[28] + " % "
## Fim bloco 2
            if linha[29] != " ":
                if linha[31] == "Empresa":
                    self.scr_valida = self.scr_valida + " AND " + linha[29] + " = " + self.empresa
                if linha[31] == "Revenda":
                    self.scr_valida = self.scr_valida + " AND " + linha[29] + " = " + self.revenda
                if linha[31] == "Data":
                    if self.bancodados == 'SQLSERVER':
                        self.scr_valida = self.scr_valida + " AND " + linha[29] + " >= " + self.data_go
                    else:
                        self.scr_valida = self.scr_valida + " AND " + linha[29] + " = TO_DATE('" + self.data_go + "', 'dd/mm/yyyy') "
                if linha[31] == "Maior que":
                    self.scr_valida = self.scr_valida + " AND " + linha[29] + " > " + linha[32]
                if linha[31] == "Menor que":
                    self.scr_valida = self.scr_valida + " AND " + linha[29] + " < " + linha[32]
                if linha[31] == "Diferente":
                    self.scr_valida = self.scr_valida + " AND " + linha[29] + " != " + linha[32]
                if linha[31] == "Igual":
                    self.scr_valida = self.scr_valida + " AND " + linha[29] + " = " + linha[32]
                if linha[31] == "IN":
                    self.scr_valida = self.scr_valida + " AND " + linha[29] + " IN (" + linha[32] + ") "
                if linha[31] == "IS NULL":
                    self.scr_valida = self.scr_valida + " AND " + linha[29] + " IS NULL "
                if linha[31] == "IS NOT NULL":
                    self.scr_valida = self.scr_valida + " AND " + linha[29] + " IS NOT NULL "
                if linha[31] == "LIKE":
                    self.scr_valida = self.scr_valida + " AND " + linha[29] + " LIKE %" + linha[32] + " % "
## Fim bloco 3
            if linha[33] != " ":
                if linha[35] == "Empresa":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " = " + self.empresa
                if linha[35] == "Revenda":+ " "
                if linha[35] == "Data":
                    if self.bancodados == 'SQLSERVER':
                        self.scr_valida = self.scr_valida + " AND " + linha[33] + " >= " + self.data_go
                    else:
                        self.scr_valida = self.scr_valida + " AND " + linha[33] + " = TO_DATE('" + self.data_go + "', 'dd/mm/yyyy') "
                if linha[35] == "Maior que":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " > " + linha[36]
                if linha[35] == "Menor que":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " < " + linha[36]
                if linha[35] == "Diferente":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " != " + linha[36]
                if linha[35] == "Igual":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " = " + linha[36]
                if linha[35] == "IN":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " IN (" + linha[36]
                if linha[35] == "IS NULL":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " IS NULL "
                if linha[35] == "IS NOT NULL":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " IS NOT NULL "
                if linha[35] == "LIKE":
                    self.scr_valida = self.scr_valida + " AND " + linha[33] + " LIKE %" + linha[36] + " % "
## Fim bloco 4
            if linha[37] != " ":
                if linha[39] == "Empresa":
                    self.scr_valida = self.scr_valida + " AND " + linha[37] + " = " + self.empresa
                if linha[39] == "Revenda":
                    self.scr_valida = self.scr_valida + " AND " + linha[37] + " = " + self.revenda
                if linha[39] == "Data":
                    if self.bancodados == 'SQLSERVER':
                        self.scr_valida = self.scr_valida + " AND " + linha[37] + " >= " + self.data_go
                    else:
                        self.scr_valida = self.scr_valida + " AND " + linha[37] + " = TO_DATE('" + self.data_go + "', 'dd/mm/yyyy') "
                if linha[39] == "Maior que":
                    self.scr_valida = self.scr_valida + " AND " + linha[37] + " > " + linha[40]
                if linha[39] == "Menor que":
                    self.scr_valida = self.scr_valida + " AND " + linha[37] + " < " + linha[40]
                if linha[39] == "Diferente":
                    self.scr_valida = self.scr_valida + " AND " + linha[37] + " != " + linha[40]
                if linha[39] == "Igual":
                    self.scr_valida = self.scr_valida + " AND " + linha[37] + " = " + linha[40]
                if linha[39] == "IN":
                    self.scr_valida = self.scr_valida + " AND " + linha[37] + " IN (" + linha[40] + ") "
                if linha[39] == "IS NULL":
                    self.scr_valida = self.scr_valida + " AND " + linha[37] + " IS NULL "
                if linha[39] == "IS NOT NULL":
                    self.scr_valida = self.scr_valida + " AND " + linha[37] + " IS NOT NULL "
                if linha[39] == "LIKE":
                    self.scr_valida = self.scr_valida + " AND " + linha[37] + " LIKE %" + linha[40] + " % "
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


