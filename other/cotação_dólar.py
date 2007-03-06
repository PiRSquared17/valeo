# -*- coding: utf-8 -*-

import urllib
import time
from socket import error
tm = time.strftime('%d/%m/%Y', time.localtime())
feriado = time.strftime('%w', time.gmtime())

print 'Aguarde....'

try:
    site = 'http://www.bcb.gov.br/htms/infecon/taxas/taxas.htm'
    getSite = urllib.urlopen(site).read()
    for line in getSite.split('</TR><tr><td ALIGN=CENTER class="fundoPadraoBClaro2">'):
        data = line[:10]
        compra = '  '+line[58:][:5]
        venda = '  '+line[112:][:5]

    if (feriado == '6'):
        fechado = u'** Sábado NÃO há cotações.             |'
    elif (feriado == '0'):
        fechado = u'** Domingo NÃO há cotações.            |'
    elif (data <> tm):
        fechado = u'** A cotação de hoje ainda NÃO fechou. |'
    else:
        fechado = u'** A cotação de hoje ESTÁ FECHADA.     |'

    """
    def printColorizedInWindows(text, color):
        std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
        for i in range(0, len(color)):
            ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color[i])
            c = text        # cor de fundo é 7
        ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)
        
        #text = u"Imprimindo texto colorido no MS-DOS"
        #color = [1] # número da cor do texto
        #printColorizedInWindows(text, color)
        return c

    cor = [10]
    tm_c = printColorizedInWindows(tm, cor)
    """
        
    show = (u"""
    +----------------------------------------+
    | Informações do Banco Central do Brasil |
    +----------------------------------------+
    |                                        |
    | Hoje é: %s::                   |
    | %s
    |                                        |
    | Fechamento do Dólar dia %s::   |       
    |  * Compra: %s                     |    
    |  * Venda:  %s                     |
    |                                        |
    +----------------------------------------+
    """%
    (tm, fechado, data, compra, venda))

    print show
    raw_input('Pressione ENTER para sair.\n')

except: 
    print '\nConexão com a internet está com problemas, tente daqui alguns segundos.\n'
    raw_input('Pressione ENTER para sair.\n')
