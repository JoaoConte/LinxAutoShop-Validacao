from Modulos import *
from Funcoes import *

class Screen():

    def datago(self):
        self.lbl_cal = Label(self.frame_selecao, text = 'Data GO-LIVE', font = ('verdana', 8, 'bold'))
        self.lbl_cal.place(relx = 0.63, rely = 0.02)
        self.ent_cal = DateEntry(self.frame_selecao, locale='pt_br')
        self.ent_cal.delete(0,END)
        self.ent_cal.place(relx=0.63, rely=0.1)

    def tela_validacao(self):

        self.telaval.title('Validação da Operação Assistida')
        self.telaval.geometry('700x650+300+20')
        self.telaval.resizable(False, False)
        self.telaval.focus_force()
        self.telaval.grab_set()
        self.telaval.iconbitmap('Linx.ico')
    # Cria as abas    
        self.tab_control = ttk.Notebook(self.telaval)           # Estanciando o controle de abas
        self.filtro = ttk.Frame(self.tab_control)               # Estanciando aba Filtro
        self.resultado = ttk.Frame(self.tab_control)            # Estanciando aba Resultados
        self.tab_control.add(self.filtro, text='Filtro')        # Definindo aba Filtro
        self.tab_control.add(self.resultado, text='Resultado')  # Definindo aba Resultado
        self.tab_control.pack(expand=1, fill='both')            # Printando abas
    # Criando os Frames
        self.frame_acesso = Frame(self.filtro, height=100, width=700)
        self.frame_selecao = Frame(self.filtro, height=550, width=700, highlightbackground="black", highlightthickness=1)
        self.frame_acesso.pack()
        self.frame_selecao.pack()

        self.le_conexao() # Le arquivo conexao.dat para identificar qual banco de dados
        if self.bancodados == 'SQLSERVER':
            self.mostra_banco = Label(self.frame_acesso, text='Banco de Dados: SQL-SERVER', font=('verdana', 15, 'bold'))
            self.mostra_banco.place(relx= 0.25, rely=0.35)
        else:
            self.mostra_banco = Label(self.frame_acesso, text='Banco de Dados: ORACLE', font=('verdana', 15, 'bold'))
            self.mostra_banco.place(relx= 0.30, rely=0.10)   
            self.lbl_usuario = Label(self.frame_acesso, text='Usuário:')
            self.lbl_usuario.place(relx=0.1, rely=0.55)
            self.ent_usuario = Entry(self.frame_acesso)
            self.ent_usuario.place(relx=0.2, rely= 0.55)
            self.lbl_senha = Label(self.frame_acesso, text='Senha:')
            self.lbl_senha.place(relx=0.6, rely=0.55)
            self.ent_senha = Entry(self.frame_acesso)
            self.ent_senha.place(relx=0.7, rely= 0.55)

            
        self.frame_revenda() # Monta lista de revendas para serem selecionadas
        self.datago()        # Seleção da data de GOLIVE
        #-----------------------------------------------------------------------
    