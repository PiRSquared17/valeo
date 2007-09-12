# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
import webbrowser, codecs
import urllib, time, httplib
try:
    from Tkinter import *
except ImportError:
    print "Tkinter não está instalado em seu sistema, por favor obtenha o pacote python-tkinter."
    
class CotadorDolar:

    copyright = 'Cotador de Dólar é software livre; você pode redistribuí-lo\n e/ou modificá-lo sobre os termos da Licença MIT.'
    autor = 'Leonardo Gregianin'
    ano = '2007'
    siteprojeto = 'http://code.google.com/p/valeo/wiki/CotadorDolar'

    tm = time.strftime('%d/%m/%Y', time.localtime())
    seg = time.strftime("%H", time.localtime())
    feriado = time.strftime('%w', time.gmtime())

    def __init__(self, parent):
        
        menubar = Menu(root)
        root.config(menu=menubar)
        root.title('Cotação diária do Dólar')
        root.geometry('350x250')

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

        self.frame3 = Frame(root)
        self.frame3.pack()
        
        self.frame4 = Frame(root)
        self.frame4.pack()
        Label(self.frame4, width=60).pack(side=LEFT)

        self.frame5 = Frame(root)
        self.frame5.pack()

        self.frame6 = Frame(root)
        self.frame6.pack()
        Label(self.frame6, width=60).pack(side=LEFT)

        self.netStatus()

    def action(self):
        webbrowser.open('http://www.bcb.gov.br/htms/infecon/taxas/taxas.htm')

    def projeto(self):
        webbrowser.open('http://code.google.com/p/valeo/wiki/CotadorDolar')

    def netStatus(self):
        try:
            urllib.urlopen('http://www.bcb.gov.br')
            Button(self.frame1, text="Informações do Banco Central do Brasil",
                   font=('Verdana, 10'), width=60, command=self.action).pack(side=LEFT)
            self.getDolar()

        except IOError:
            texto = 'Sua conexão com a internet ou o site do\n Banco Central está com problemas,\n tente novamente daqui alguns segundos.'
            Label(self.frame3, text=texto, font=('Verdana, 10'), width=60, bg='red').pack(side=LEFT)
                
    def getDolar(self):
        url = 'http://www.bcb.gov.br/htms/infecon/taxas/taxas.htm'
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)

        cotacao = soup.findAll('td')[-3:]
        data, compra, venda = [td.string for td in cotacao]

        if (self.feriado == '6'):
            fechado = 'Hoje é %s, Sábado não há cotações' % self.tm
        elif (self.feriado == '0'):
            fechado = 'Hoje é %s, Domingo não há cotações' % self.tm
        elif (data <> self.tm):
            if self.seg >= '16':
                fechado = 'O site do Banco Central ainda não atualizou a cotação de hoje'
            else:
                fechado = 'A cotação de hoje %s ainda não fechou' % self.tm
        elif (data == self.tm):
            fechado = 'A cotação de hoje %s está fechada' % self.tm

        status = Label(root, text=fechado, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
        texto = u'\nCotação do dia %s\n\n Compra: %s\n Venda: %s\n' % (data, compra, venda)
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
