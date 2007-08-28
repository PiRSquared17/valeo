# -*- coding: utf-8 -*-

import wikipedia
import time, re, gui

if __name__ == '__main__':
    
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
    
    site = wikipedia.getSite('pt', 'wikiquote')
    template = 'Template:Frase_do_dia/%s' % today
    page = wikipedia.Page(site, template)
    text = page.get()
    
    r = re.search('(?<=frase=)(.+)', text)
    m = re.search('(?<=autor=)(.+)', text)
    quote = """\n%s \n\n%s \n\n\nFonte: http://pt.wikiquote.org""" % (r.group(0), m.group(0))
    myapp = gui.EditBoxWindow()
    myapp.edit(quote)
