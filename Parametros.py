from Modulos import *

class Param():
    def padrao_auto(self):
        self.cb_contabil.select()
        self.cb_crm.deselect()
        self.cb_div.select()
        self.cb_financeiro.select()
        self.cb_mobile.deselect()
        self.cb_oficina.select()
        self.cb_pecas.select()
        self.cb_veiculos.deselect()
        self.cb_fiscal.select()

    def padrao_dms(self):
        self.cb_contabil.select()
        self.cb_crm.select()
        self.cb_div.select()
        self.cb_financeiro.select()
        self.cb_mobile.select()
        self.cb_oficina.select()
        self.cb_pecas.select()
        self.cb_veiculos.select()
        self.cb_fiscal.select()

    def le_par(self):
        self.conecta_voa()
        modulopar = self.cursor_voa.execute('SELECT * from modulos')
        for linhapar in modulopar:
            if linhapar[0] == 'CONTABILIDADE':
                if linhapar[1] == 'S':
                    self.cb_contabil.select()
                else:
                    self.cb_contabil.deselect()
            if linhapar[0] == 'CRM':
                if linhapar[1] == 'S':
                    self.cb_crm.select()
                else:
                    self.cb_crm.deselect()
            if linhapar[0] == 'DIVERSOS':
                if linhapar[1] == 'S':
                    self.cb_div.select()
                else:
                    self.cb_div.deselect()
            if linhapar[0] == 'FINANCEIRO':
                if linhapar[1] == 'S':
                    self.cb_financeiro.select()
                else:
                    self.cb_financeiro.deselect()
            if linhapar[0] == 'MOBILE-DMS':
                if linhapar[1] == 'S':
                    self.cb_mobile.select()
                else:
                    self.cb_mobile.deselect()
            if linhapar[0] == 'OFICINA':
                if linhapar[1] == 'S':
                    self.cb_oficina.select()
                else:
                    self.cb_oficina.deselect()
            if linhapar[0] == 'PECAS':
                if linhapar[1] == 'S':
                    self.cb_pecas.select()
                else:
                    self.cb_pecas.deselect()
            if linhapar[0] == 'VEICULOS':
                if linhapar[1] == 'S':
                    self.cb_veiculos.select()
                else:
                    self.cb_veiculos.deselect()
            if linhapar[0] == 'FISCAL':
                if linhapar[1] == 'S':
                    self.cb_fiscal.select()
                else:
                    self.cb_fiscal.deselect()
        self.desconecta_voa()

    def cad_par(self):
        self.telapar = Toplevel()
        self.telapar.title('Parâmetros')
        self.telapar.geometry('400x500+450+150')
        self.telapar.resizable(False, False)
        self.telapar.transient(self.principal)
        self.telapar.focus_force()
        self.telapar.grab_set()
        self.telapar.iconbitmap('Linx.ico')

        self.cbt_contabil = IntVar()
        self.cbt_crm = IntVar()
        self.cbt_div = IntVar()
        self.cbt_financeiro = IntVar()
        self.cbt_oficina = IntVar()
        self.cbt_pecas = IntVar()
        self.cbt_veiculos = IntVar()
        self.cbt_mobile = IntVar()
        self.cbt_fiscal = IntVar()

        self.texto = Label(self.telapar, text = 'Módulos a serem validados', font=('verdana', 15, 'bold' ))
        self.texto.place(relx = 0.1, rely = 0.05)
        self.cb_contabil = Checkbutton(self.telapar, text ='Contabilidade', variable = self.cbt_contabil, onvalue=1, offvalue=0)
        self.cb_contabil.place(relx = 0.1, rely = 0.15)
        self.cb_crm = Checkbutton(self.telapar, text='CRM', variable = self.cbt_crm, onvalue=1, offvalue=0)
        self.cb_crm.place(relx=0.1, rely=0.24)
        self.cb_div = Checkbutton(self.telapar, text='Modulos Diversos', variable = self.cbt_div, onvalue=1, offvalue=0)
        self.cb_div.place(relx=0.1, rely=0.33)
        self.cb_financeiro = Checkbutton(self.telapar, text='Financeiro', variable = self.cbt_financeiro, onvalue=1, offvalue=0)
        self.cb_financeiro.place(relx=0.1, rely=0.42)
        self.cb_oficina = Checkbutton(self.telapar, text='Oficina', variable = self.cbt_oficina, onvalue=1, offvalue=0)
        self.cb_oficina.place(relx=0.1, rely=0.51)
        self.cb_pecas = Checkbutton(self.telapar, text='Peças', variable = self.cbt_pecas, onvalue=1, offvalue=0)
        self.cb_pecas.place(relx=0.1, rely=0.60)
        self.cb_veiculos = Checkbutton(self.telapar, text='Veiculos', variable = self.cbt_veiculos, onvalue=1, offvalue=0)
        self.cb_veiculos.place(relx=0.1, rely=0.69)
        self.cb_mobile = Checkbutton(self.telapar, text='Mobile DMS', variable = self.cbt_mobile, onvalue=1, offvalue=0)
        self.cb_mobile.place(relx=0.1, rely=0.78)
        self.cb_fiscal = Checkbutton(self.telapar, text='Fiscal', variable=self.cbt_fiscal, onvalue=1, offvalue=0)
        self.cb_fiscal.place(relx=0.1, rely=0.87)
        self.le_par()

        self.bt_pdauto = Button(self.telapar, text='Padrão Linx AutoShop', bg = '#D3D3D3', font=('verdana', 9, 'bold'), command=self.padrao_auto)
        self.bt_pdauto.place(width=160, height= 30, relx=0.5, rely=0.40)

        self.bt_pdldms = Button(self.telapar, text='Padrão Linx DMS', bg = '#D3D3D3', font=('verdana', 9, 'bold'), command=self.padrao_dms)
        self.bt_pdldms.place(width=160, height= 30, relx=0.5, rely=0.50)

        self.bt_salva_par = Button(self.telapar, text='Salvar e Fechar', bg = '#D3D3D3', font=('verdana', 9, 'bold'), command = self.grava_par)
        self.bt_salva_par.place(width=160, height= 30, relx = 0.5, rely = 0.87)

    def grava_par(self):
        self.conecta_voa()
        if self.cbt_contabil.get() == 1:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'S' WHERE codigo = 'CONTABILIDADE'")
        else:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'N' WHERE codigo = 'CONTABILIDADE'")
        if self.cbt_crm.get() == 1:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'S' WHERE codigo = 'CRM'")
        else:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'N' WHERE codigo = 'CRM'")
        if self.cbt_div.get() == 1:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'S' WHERE codigo = 'DIVERSOS'")
        else:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'N' WHERE codigo = 'DIVERSOS'")
        if self.cbt_financeiro.get() == 1:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'S' WHERE codigo = 'FINANCEIRO'")
        else:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'N' WHERE codigo = 'FINANCEIRO'")
        if self.cbt_oficina.get() == 1:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'S' WHERE codigo = 'OFICINA'")
        else:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'N' WHERE codigo = 'OFICINA'")
        if self.cbt_pecas.get() == 1:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'S' WHERE codigo = 'PECAS'")
        else:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'N' WHERE codigo = 'PECAS'")
        if self.cbt_veiculos.get() == 1:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'S' WHERE codigo = 'VEICULOS'")
        else:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'N' WHERE codigo = 'VEICULOS'")
        if self.cbt_mobile.get() == 1:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'S' WHERE codigo = 'MOBILE-DMS'")
        else:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'N' WHERE codigo = 'MOBILE-DMS'")
        if self.cbt_fiscal.get() == 1:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'S' WHERE codigo = 'FISCAL'")
        else:
            self.cursor_voa.execute("UPDATE modulos SET ativo = 'N' WHERE codigo = 'FISCAL'")
        self.banco_voa.commit()
        self.desconecta_voa()
        self.telapar.destroy()




