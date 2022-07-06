from Modulos import *

class Conexao():
    def le_conexao(self):  # Lê ..\conexao.dat
        self.caminho = os.path.abspath(os.path.dirname('.')) # Pega diretorio atual
        try:
            with open(self.caminho + '\conexao.dat', 'r') as conecta:
                for self.leitura in conecta:
                    if self.leitura[0:12] == '[BANCODADOS]':
                        self.bancodados = self.leitura[13:]
                        self.bancodados = self.bancodados.strip("\n")
                        if self.bancodados == 'SQLSERVER':
                            self.drive = "SQL Server"
                    if self.leitura[0:10] == '[DATABASE]':
                        if self.bancodados == 'SQLSERVER':
                            self.posp = self.leitura.find(':')
                            self.servidor = self.leitura[11:self.posp]
                            self.banco1 = self.leitura[self.posp + 1:]
                            self.banco = self.banco1.strip("\n")
                        else:
                            self.posp = self.leitura.find('/')
                            self.banco1 = self.leitura[11:self.posp]
                            self.banco2 = self.leitura[self.posp + 1:]
                            self.bancoa = self.banco1.strip('\n')
                            self.bancob = self.banco2.strip('\n')
                    if self.leitura[0:16] == '[USUARIO_ORACLE]':
                        self.usuario1 = self.leitura[17:]
                        self.usuario = self.usuario1.strip('\n')
                        self.senha = 'ninguemsabe'
            if self.bancodados != 'SQLSERVER':
                self.ora_conn = (usuario+"/"+senha+"@"+ bancoa+"/"+bancob)
                self.ora_conn = ('linx/ninguemsabe@contevaio/XE')

        except OSError:
            messagebox.showerror(title='Falha na conexão com o Banco de dados', message='Banco de dados nao encontrado!\n'
                                                                                        'Verifique se o programa executor esta na pasta do sistema\n '
                                                                                        'ou se na pasta atual tem o arquivo conexao.dat')

    def conecta_DB(self):
        if self.bancodados != 'SQLSERVER':
            self.cbd_ora = cx_Oracle.connect('linx/ninguemsabe@contevaio/XE')
            self.cursor = self.cbd_ora.cursor()
        else:
            self.cbd_sql = pyodbc.connect(
                "Driver=" + self.drive + "; Server=" + self.servidor + "; Database=" + self.banco + "; TrustedConnection=yes")
            self.cursor = self.cbd_sql.cursor()

    def desconecta_DB(self):
        if self.bancodados != 'SQLSERVER':
            self.cbd_ora.close()
        else:
            self.cbd_sql.close()

    def conecta_voa(self):
        caminho = os.path.abspath(os.path.dirname('.'))
        self.banco_voa = sqlite3.connect(caminho+"\VAL_SCRIPT.db")
        self.cursor_voa = self.banco_voa.cursor()

    def desconecta_voa(self):
        self.banco_voa.close()
