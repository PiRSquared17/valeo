# -*- coding: utf-8 -*-

import time, re
import wikipedia
from Tkinter import *

__version__ = '0.3'

# Contribuintes:
# Walter Cruz

class FrasedoDia(object):

    def __init__(self, parent):
        meses = ('Janeiro','Fevereiro',u'Março','Abril',
        'Maio','Junho','Julho','Agosto','Setembro','Outubro',
        'Novembro','Dezembro')
        now = time.localtime()
        year = time.strftime('%Y',now)
        month = meses[now.tm_mon - 1]
        day = now.tm_mday
        self.today = '%s_de_%s' % (day, month)
        self._today = '%s de %s de %s' % (day, month, year)
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
email: leogregianin@gmail.com''' % __version__)

    def Quit(self):
        root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = FrasedoDia(root)
    root.mainloop()
