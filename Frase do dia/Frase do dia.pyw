# -*- coding: utf-8 -*-

import time, re, sys
try:
    from Tkinter import *
except ImportError:
    print "Tkinter não está instalado em seu sistema, por favor obtenha o pacote python-tkinter."
    
try:
    import wikipedia
except:
    print "Você não tem a biblioteca wikipedia, veja em http://sf.net/projects/pywikipediabot"
    sys.exit()

class FrasedoDia:

    copyright = '"Frase do Dia" é software livre; você pode redistribuí-lo\n e/ou modificá-lo sobre os termos da Licença MIT.'
    autor = 'Leonardo Gregianin'
    ano = '2007'
    siteprojeto = 'http://code.google.com/p/valeo/wiki/FrasedoDia'

    dia = time.strftime('%d', time.localtime())
    mes = time.strftime('%m', time.localtime())

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

    today = '%s_de_%s' % (dia, mes)
     
    def __init__(self, parent):
        
        menubar = Menu(root)
        root.config(menu=menubar)
        root.title('Frase do Dia')
        root.geometry('450x320')

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
        
        self.frame4 = Frame(root)
        self.frame4.pack()
        Label(self.frame4, width=60).pack(side=LEFT)

        self.frame5 = Frame(root)
        self.frame5.pack()

        self.frame6 = Frame(root)
        self.frame6.pack()
        Label(self.frame6, width=60).pack(side=LEFT)

        self.getQuote()

    def projeto(self):
        webbrowser.open('http://code.google.com/p/valeo/wiki/FrasedoDia')

    def getQuote(self):
        site = wikipedia.getSite('pt', 'wikiquote')
        template = 'Template:Frase_do_dia/%s' % self.today
        page = wikipedia.Page(site, template)
        text = page.get()
    
        r = re.search('(?<=frase=)(.+)', text)
        m = re.search('(?<=autor=)(.+)', text)
        quote = """\n%s \n\n%s \n\n\nFonte: http://pt.wikiquote.org""" % (r.group(0), m.group(0))

        text = Text(self.frame2)
        text.pack();
        text.insert('insert', quote)

    def About(self):
        root = Tk()
        root.title('Sobre a Frase do Dia')
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
    app = FrasedoDia(root)
    root.mainloop()
