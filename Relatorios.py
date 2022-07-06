from Modulos import *

class Rel_valida():
    def printRel(self):
        webbrowser.open(self.modulo+'.pdf')

    def geraRel(self, texto, listav):
        posx = 0
        posy = 1380
        self.listas = listav
        self.texto_val = texto
        self.c = canvas.Canvas(self.modulo + '.pdf')
        self.c.setTitle(self.modulo + '.pdf')
        self.data_atu = datetime.today().strftime('%d/%m/%Y')
        logo = 'linx.png'
        self.c.drawImage(logo, 30, 725, width=100, height=100)
        self.c.setFont('Helvetica-Bold', 20)
        var1 = 'Validação da Operação Assistida'
        var2 = (345-(len(var1)*4.5))
        self.c.drawString(var2, 770, var1)
        self.c.setFont('Helvetica-Bold', 12)
        self.c.drawCentredString(300, 675,'Loja: ' + self.combo_p)
        self.c.setFont('Helvetica-Bold', 15)
        self.c.drawString(220, 655, 'Módulo: '+ self.modulo)
        self.c.setFont('Helvetica-Bold', 15)
        self.c.drawString(50, 700, self.texto_val + self.data_atu)
        if self.contador == 0:
            self.c.drawString(390, 700, 'Data Go-Live: ' + self.data_go)
        self.c.setFont('Helvetica', 10)
        conta = 630
        for self.lista in self.listas:
            self.c.drawString(20, conta, self.lista)
            conta = conta -13
        if self.contador == 0:
            self.c.setFont('Helvetica-Bold', 10)
            self.c.drawString(45,12,'Documento dispensa assinatura, pois o mesmo só pode ser emitido quando todos os itens estiverem validados.')
        self.c.showPage()
        self.c.save()
        self.printRel()
