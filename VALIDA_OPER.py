from Modulos import *
from Relatorios import *
from Funcoes import Funcs
from Screen_frame import *
from Validacao import *
from GravaTabelas import *
from Conecta_banco import *
from Parametros import *

# Carga dos modulos

principal = Tk()#tix.Tk() # Estanciando a intergace grafica

class Application(Funcs, Rel_valida, Screen, Valida, Conexao, Grava, Param): # Declarando uso das classes
 # Inicialização em tempo de carga
    def __init__(self):
        self.principal = principal
        self.le_conexao()
        self.tela()
        self.btn_principal()
        self.cria()
        self.Menus()
        self.principal.mainloop()
# Criacao do menu superior
    def Menus(self):
        menubar = Menu(self.principal)
        self.principal.config(menu=menubar)
        config_menu = Menu(menubar, tearoff=0)
        valida_menu = Menu(menubar, tearoff=0)
        sair_menu = Menu(menubar, tearoff=0)
# Destroi o formulario e sai do sistema
        def Sair():
            self.principal.destroy()
# Implementa funcionalidades aos menus
        menubar.add_cascade(label='Configurações', menu=config_menu)
        menubar.add_cascade(label='Validação', menu=valida_menu)
        menubar.add_cascade(label='Sobre', menu=sair_menu)
        config_menu.add_command(label='Parametros', command=self.cad_par)
        config_menu.add_command(label='Cadastros', command=self.tela_cadastro)
        config_menu.add_command(label='Sair', command=Sair)
        valida_menu.add_command(label='Validar', command=self.tela_validacao)
        sair_menu.add_command(label='Sobre')#, command=self.tela_sobre)

Application()