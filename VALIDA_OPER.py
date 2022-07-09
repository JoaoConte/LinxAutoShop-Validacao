from Modulos import *
from Relatorios import *
from Funcoes import Funcs
from Screen_frame import *
from Validacao import *
from Conecta_banco import *

# Carga dos modulos

telaval = Tk()#tix.Tk() # Estanciando a intergace grafica

class Application(Funcs, Rel_valida, Screen, Valida, Conexao): # Declarando uso das classes
 # Inicialização em tempo de carga
    def __init__(self):
        self.telaval = telaval
        self.le_conexao()
        self.tela_validacao()
        self.cria()
        self.telaval.mainloop()

Application()