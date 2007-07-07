#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

class Dolar:
    def __init__(self, toplevel):

        # Janela
        toplevel.title('Cotação do Dólar')
        toplevel.geometry("350x250")

        # Espaçamento
        self.frame1 = Frame(toplevel)
        self.frame1.pack()

        # Data hoje
        self.frame2 = Frame(toplevel)
        self.frame2.pack()

        # Dolar já fechou hoje
        self.frame3 = Frame(toplevel)
        self.frame3.pack()

        # Cotação dia do BC site
        self.frame4 = Frame(toplevel)
        self.frame4.pack()

        # Compra
        self.frame5 = Frame(toplevel)
        self.frame5.pack()

        # Venda
        self.frame6 = Frame(toplevel)
        self.frame6.pack()

        # Botões
        self.frame8 = Frame(toplevel)
        self.frame8.pack()

        ##################

        # Cor e tamanho das letras 
        Label(self.frame1,text='', fg='black',
        font=('Verdana','10'), height=1).pack()
        fonte1=('Verdana','10')

        # Botão Atualizar
        atualizar=Button(self.frame8, font=fonte1, text= 'Atualizar', command=self.atualizar)
        atualizar.pack(side=LEFT)

        # Botão Sair
        sair=Button(self.frame8, font=fonte1, text= 'Sair', command=self.sair)
        sair.pack(side=LEFT)

        ###################
        
        # Frame 2 - data
        Label(self.frame2,text='Data de hoje: ',font=fonte1,width=30).pack(side=LEFT)
        self.msg=Label(self.frame2,width=10,font=fonte1)
        self.msg.pack(side=LEFT)

        # Frame 3 - data do bc
        Label(self.frame3,text='Cotação de hoje já fechou... ',font=fonte1,width=30).pack(side=LEFT)
        self.msg=Label(self.frame3, width=10, font=fonte1)
        self.msg.pack(side=LEFT)

        # Frame 4 - cotação
        Label(self.frame4,text='Cotação que está no site do bc é: ',font=fonte1,width=30).pack(side=LEFT)
        self.msg=Label(self.frame4, width=10, font=fonte1)
        self.msg.pack(side=LEFT)

        # Frame 5
        Label(self.frame5, text='Compra: ', font=fonte1, width=10).pack(side=LEFT)
        self.msg=Label(self.frame5, width=5, font=fonte1)
        self.msg.pack(side=LEFT)

        # Frame 6
        Label(self.frame6, text='Venda: ', font=fonte1, width=10).pack(side=LEFT)
        self.msg=Label(self.frame6, width=5, font=fonte1)
        self.msg.pack(side=LEFT)

    def cotacaocompra(self):
        dolarcompra = '1,8'
        w = Message(self.frame5, text=dolarcompra, font=('Verdana','10'))
        w.pack()

        #dolarcompra = '1,89'
        #self.msg['text']= '%s' % dolarcompra

    def cotacaovenda(self):
        dolarvenda = '1,9'
        w = Message(self.frame6, text=dolarvenda, font=('Verdana','10'))
        w.pack()

        #dolarvenda = '1,90'
        #self.msg['text']= '%s' % dolarvenda

    def atualizar(self):
        self.cotacaovenda()
        self.cotacaocompra()

    def sair(self):
        app.destroy()

app=Tk()
Dolar(app)
app.mainloop()
