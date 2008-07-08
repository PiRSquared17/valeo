# -*- coding: utf-8 -*-

import time, re
import wikipedia
from Tkinter import *

__version__ = '0.2'

class FrasedoDia:

    dia = time.strftime('%d', time.localtime())
    mes = time.strftime('%m', time.localtime())
    ano = time.strftime('%y', time.localtime())

    if dia == '01': dia = '1'
    if dia == '02': dia = '2'
    if dia == '03': dia = '3'
    if dia == '04': dia = '4'
    if dia == '05': dia = '5'
    if dia == '06': dia = '6'
    if dia == '07': dia = '7'
    if dia == '08': dia = '8'
    if dia == '09': dia = '9'
    
    if mes == '01': mes = 'Janeiro'
    if mes == '02': mes = 'Fevereiro'
    if mes == '03': mes = u'Março'
    if mes == '04': mes = 'Abril'
    if mes == '05': mes = 'Maio'
    if mes == '06': mes = 'Junho'
    if mes == '07': mes = 'Julho'
    if mes == '08': mes = 'Agosto'
    if mes == '09': mes = 'Setembro'
    if mes == '10': mes = 'Outubro'
    if mes == '11': mes = 'Novembro'
    if mes == '12': mes = 'Dezembro'

    if ano == '08': ano = '2008'
    if ano == '09': ano = '2009'
    if ano == '10': ano = '2010'
    if ano == '11': ano = '2011'
    if ano == '12': ano = '2012'

    today = '%s_de_%s' % (dia, mes)
    _today = '%s de %s de %s' % (dia, mes, ano)

    def __init__(self, parent):

        menubar = Menu(root)
        root.config(menu=menubar)
        root.title('Frase do dia %s' % self._today)
        root.geometry('450x320')

        filemenu1 = Menu(menubar)
        filemenu2 = Menu(menubar)

        menubar.add_cascade(label='Arquivo', menu=filemenu1)
        menubar.add_cascade(label='Ajuda', menu=filemenu2)

        filemenu1.add_command(label='Sair', command=self.Quit)
        filemenu2.add_command(label='Abrir http://pt.wikiquote.org', command=self.Quote)
        filemenu2.add_command(label='Sobre', command=self.About)

        self.frame1 = Frame(root)
        self.frame1.pack()
        
        self.frame2 = Frame(root)
        self.frame2.pack()
        
        self.frame4 = Frame(root)
        self.frame4.pack()
        Label(self.frame4, width=60).pack(side=LEFT)

        self.frame5 = Frame(root)
        self.frame5.pack()

        self.frame6 = Frame(root)
        self.frame6.pack()
        Label(self.frame6, width=60).pack(side=LEFT)

        self.getQuote()

    def getQuote(self):
        site = wikipedia.getSite('pt', 'wikiquote')
        template = 'Template:Frase_do_dia/%s' % self.today
        page = wikipedia.Page(site, template)
        text = page.get()
    
        r = re.search('(?<=frase=)(.+)', text)
        m = re.search('(?<=autor=)(.+)', text)
        quote = """\n%s \n\n%s \n""" % (r.group(0), m.group(0))

        text = Text(self.frame2, font=('Verdana, 12'))
        text.pack()
        text.insert('insert', quote)
        
    def Quote(self):
        import webbrowser
        webbrowser.open("http://pt.wikiquote.org", 1)

    def About(self):
        import tkMessageBox
        tkMessageBox.showinfo('Frase do Dia %s' % __version__,
                              u'''\
Frase do Dia %s

Citação do dia pelo
site pt.wikiquote.org

Informações
contato: Leonardo Gregianin
email:   leogregianin@gmail.com''' % __version__)

    def Quit(self):
        root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = FrasedoDia(root)
    root.mainloop()
