# -*- coding: utf-8 -*-

from BeautifulSoup import *
import urllib

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

