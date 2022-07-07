from Modulos import *
from Funcoes import *

class Screen():

    def tela(self):
        self.principal.title('Validação de Operação Assistida')  # Titulo da janela
        self.principal.geometry('840x400+250+150')  # Tamanho inicial da tela
        #self.principal.configure(bg = '#422256')  # '#48185b
        self.principal.resizable(False, False)  # Redimencionamento (default = True)
        self.principal.iconbitmap('Linx.ico')


 
 #######***********************************************************************************************************************
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

        self.desconecta_voa()
        #self.telaval = Toplevel(self.principal)
        self.telaval.title('Validação da Operação Assistida')
        self.telaval.geometry('700x650+300+20')
        self.telaval.resizable(False, False)
        #self.telaval.transient(self.principal)
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

