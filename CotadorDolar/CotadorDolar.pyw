# -*- coding: utf-8 -*-

'''
todo:
gravar valores (pickle, shelve, sqlite, ...)
obter valores reais para o gráfico

'''

import webbrowser, codecs
import urllib, time, httplib
try:
    from Tkinter import *
    import tkFileDialog
except ImportError:
    print ("Tkinter não está instalado em seu sistema, por favor obtenha o pacote python-tkinter.")
    
class CotadorDolar:

    copyright = 'Cotador de Dólar é software livre; você pode redistribuí-lo\n e/ou modificá-lo sobre os termos da Licença MIT.'
    autor = 'Leonardo Gregianin'
    ano = '2007'
    siteprojeto = 'http://code.google.com/p/valeo/wiki/CotadorDolar'

    tm = time.strftime('%d/%m/%Y', time.localtime())
    seg = time.strftime("%H", time.localtime())
    feriado = time.strftime('%w', time.gmtime())

    ######################################################################################
    # Substituir por BeautifulSoup.py                                                    #
    ######################################################################################
    site = 'http://www.bcb.gov.br/htms/infecon/taxas/taxas.htm'
    getSite = urllib.urlopen(site).read()
    for line in getSite.split('</TR><tr><td ALIGN=CENTER class="fundoPadraoBClaro2">'):
        data = line[:10]
        compra = ' '+line[58:][:5]
        venda = ' '+line[112:][:5]
    ######################################################################################
 
    def __init__(self, parent):
        
        menubar = Menu(root)
        root.config(menu=menubar)
        root.title('Cotador de Dólar')
        root.geometry('480x535')

        filemenu1 = Menu(menubar)
        filemenu2 = Menu(menubar)

        menubar.add_cascade(label='Ações', menu=filemenu1)
        menubar.add_cascade(label='Ajuda', menu=filemenu2)

        filemenu1.add_command(label='Sair', command=self.Quit)
        filemenu2.add_command(label='Sobre', command=self.About)

        self.frame1 = Frame(root)
        self.frame1.pack()
        
        self.frame2 = Frame(root)
        self.frame2.pack()
        
        #self.frame3 = Frame(root)
        #self.frame3.pack()

        self.frame4 = Frame(root)
        self.frame4.pack()
        Label(self.frame4, width=60).pack(side=LEFT)

        self.frame5 = Frame(root)
        self.frame5.pack()

        self.frame6 = Frame(root)
        self.frame6.pack()
        Label(self.frame6, width=60).pack(side=LEFT)

        self.netStatus()

    def Graph(self):

        # fundo
        graph = Canvas(self.frame5, width=440, height=290, background='white')

        # horizontal borda
        graph.create_line (50, 250, 400, 250, fill='black')
        graph.create_line (50, 50, 400, 50, fill='black')
        
        # vertical borda
        graph.create_line (50, 50, 50, 250, fill='black')
        graph.create_line (400, 50, 400, 250, fill='black')

        # vertical meio
        graph.create_line (100, 50, 100, 250, fill='gray')
        graph.create_line (150, 50, 150, 250, fill='gray')
        graph.create_line (200, 50, 200, 250, fill='gray')
        graph.create_line (250, 50, 250, 250, fill='gray')
        graph.create_line (300, 50, 300, 250, fill='gray')
        graph.create_line (350, 50, 350, 250, fill='gray')

        # horizontal meio
        graph.create_line (50, 100, 400, 100, fill='gray')
        graph.create_line (50, 150, 400, 150, fill='gray')
        graph.create_line (50, 200, 400, 200, fill='gray')
                
        # valores
        graph.create_line (50,  250, 100, 200, fill='red', width='5')
        graph.create_line (100, 200, 150, 200, fill='red', width='5')
        graph.create_line (150, 200, 200, 150, fill='red', width='5')
        graph.create_line (200, 150, 250, 150, fill='red', width='5')
        graph.create_line (250, 150, 300, 100, fill='red', width='5')
        graph.create_line (300, 100, 350, 100, fill='red', width='5')

        # Coordenada x (dias da semana)
        graph.create_text (100, 260, text='Sexta', fill='black')
        graph.create_text (150, 260, text='Segunda', fill='black')
        graph.create_text (200, 260, text='Terça', fill='black')
        graph.create_text (250, 260, text='Quarta', fill='black')
        graph.create_text (300, 260, text='Quinta', fill='black')
        graph.create_text (350, 260, text='Sexta', fill='black')

        # Coordenada y (valores de referência)
        graph.create_text (30, 250, text='1,00', fill='black')
        graph.create_text (30, 200, text='1,50', fill='black')
        graph.create_text (30, 150, text='2,00', fill='black')
        graph.create_text (30, 100, text='2,50', fill='black')
        graph.create_text (30, 50, text='3,00', fill='black')

        graph.pack()

    def action(self):
        webbrowser.open('http://www.bcb.gov.br/htms/infecon/taxas/taxas.htm')

    def projeto(self):
        webbrowser.open('http://code.google.com/p/valeo/wiki/CotadorDolar')

    def netStatus(self):
        try:
            urllib.urlopen('http://www.bcb.gov.br')
            Button(self.frame1, text="Informações do Banco Central do Brasil",
                   font=('Verdana, 10'), width=60, command=self.action).pack(side=LEFT)
            self.getStatus()
            self.getDolar()
            self.Graph()
        except IOError:
            texto = 'Sua conexão com a internet ou o site do Banco Central\n está com problemas, tente novamente daqui alguns segundos.'
            Label(self.frame3, text=texto, font=('Verdana, 10'), width=60, bg='red').pack(side=LEFT)
                
    def getStatus(self):
        if (self.feriado == '6'):
            fechado = 'Hoje é %s, Sábado não há cotações' % self.tm
        elif (self.feriado == '0'):
            fechado = 'Hoje é %s, Domingo não há cotações' % self.tm
        elif (self.data <> self.tm):
            if self.seg >= '16':
                fechado = 'O site do Banco Central ainda não atualizou a cotação de hoje'
            else:
                fechado = 'A cotação de hoje %s ainda não fechou' % self.tm
        elif (self.data == self.tm):
            fechado = 'A cotação de hoje %s está fechada' % self.tm

        status = Label(root, text=fechado, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

    def getDolar(self):
        dia = self.data
        cotacao_compra = self.compra
        cotacao_venda = self.venda
        texto = '\nCotação do dia %s\n\n Compra: %s\n Venda: %s\n' % (dia, cotacao_compra, cotacao_venda)
        Label(self.frame2, text=texto, font=('Verdana, 14'), width=60).pack(side=LEFT)

    def About(self):
        root = Tk()
        root.title('Sobre o Cotador de Dólar')
        root.geometry('400x250')
        text = Label(root)
        text2 = Label(root)
        text.pack()
        text2.pack()
        creditos = ('\n%s\n\n%s, %s\n' % (self.copyright, self.autor, self.ano))
        Label(text, text=creditos, font=('Verdana, 10'), width=60).pack(side=LEFT)
        Button(text2, text=self.siteprojeto, font=('Verdana, 10'), command=self.projeto).pack(side=LEFT)

    def Site(self):
        webbrowser.open("%s" % self.site)

    def Quit(self):
        root.destroy()
                
if __name__ == "__main__":
    root = Tk()
    app = CotadorDolar(root)
    root.mainloop()
