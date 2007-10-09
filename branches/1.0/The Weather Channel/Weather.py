# -*- coding: utf-8 -*-
'''
The Weather Channel
   Preferências: 
        cidade (mapear todos os zip codes)
        medida: ºC ou ºF
        língua

   gravar cidade, medida e língua de preferência
   
   Mostrar:
        Temperatura
        Humidade
        Visibilidade
        Vento
        Pressão
        Nascer do sol
        Pôr do sol
        Ponto de orvalho
        Sensação térmica
        Índice de raios ultra-violetas
        Última atualização
        Condição do tempo: Sol, Chuva, Fumaça, Nublado, ...
        Imagem da condição do tempo
        Tempo de amanhã: temperatura e chances de chuva

'''

from BeautifulSoup import *
from urllib import urlopen
import urllib

class FirefoxFaker(urllib.URLopener):
    version = "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1b1) Gecko/20060601 Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.4) Gecko/20060508 Firefox/1.5.0.4 (Ubuntu-edgy)"

    def __init__(self, *args):
        urllib.URLopener.__init__(self)

urllib._urlopener = FirefoxFaker()

varzea_grande = 'BRXX0255'
url = 'http://www.weather.com/outlook/travel/businesstraveler/local/%s' % varzea_grande
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

condicao = soup.find('strong', {'class':'obsTextA'}).string
if condicao == u'Thunder':
    condicao = u'Trovoada'
elif condicao == u'Smoke':
    condicao = u'Fumaça'
elif condicao == u'Fair':
    condicao = u'Céu claro'
print u'Condição do tempo: %s' % condicao

temperatura = soup.find('strong', {'class':'obsTempTextA'}).string

temperatura_soh_numero = int(temperatura.replace(u'&deg;F', u''))
temperatura_F_para_C = (temperatura_soh_numero-32)/1.8

temperatura_subst = temperatura.replace(u'&deg;', u'º')
print u'Temperatura: %s ou %sºC' % (temperatura_subst, int(temperatura_F_para_C))

#sensacao = soup.find('strong', {'class':'obsTextA'}).string
#print u'Sensação térmica: %s' % sensacao

updated = soup.find('div', {'class':'updated'}).string
updated_subst = updated.replace(u'Updated: ', u'Atualizado em:') 
print updated_subst

