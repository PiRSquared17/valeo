# -*- coding: utf-8 -*-

import urllib
import time
tm = time.strftime('%d/%m/%Y', time.localtime())
feriado = time.strftime('%w', time.gmtime())

def dolar():
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

if __name__ == '__main__':
    try:
        dolar()
    except:
        try: dolar()
        except:
            print u'\nConexão com a internet está com problemas,\ntente daqui alguns segundos.\n'
