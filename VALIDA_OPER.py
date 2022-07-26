from Modulos import *         # Seção onde são carregadas todas as bibliotecas utilizadas 
from Relatorios import *      # Rotina para geração de relatórios e apresentação em tela
from Funcoes import Funcs     # Principais funções do sistema
from Screen_frame import *    # Principais rotinas (parte da regra de negócios)
from Validacao import *       # Rotina de montagem e validação dos scripts (leitura do banco VAL_SCRIPT.db)
from Conecta_banco import *   # Rotina de conexão aos bancos utilizados neste sistema (SQLITE3 e SQL-SERVER/ORACLE)

# Carga dos modulos

telaval = Tk() #tix.Tk() # Estanciando a intergace grafica

class Application(Funcs, Rel_valida, Screen, Valida, Conexao): # Declarando uso das classes
 # Inicialização em tempo de carga
    def __init__(self):
        self.telaval = telaval  # Estância tela inicial
        self.le_conexao()       # Efetua leitura do conexão.dat
        self.tela_validacao()   # Carrega tela inicial do sistema
        self.telaval.mainloop() # Engine do TKINTER

Application()