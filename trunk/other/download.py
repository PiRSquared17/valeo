# -*- coding: utf-8 -*-

import httplib, urllib

def imagem():
    headers = {"Accept": "image/gif"}
    conn = httplib.HTTPConnection('www.python.org')
    conn.request("GET", "/images/python-logo.gif", None, headers)
    r = conn.getresponse()
    print r.status, r.reason
    data = r.read()
    arq = open("C:\\Documents and Settings\\Proprietario\\Desktop\\teste.gif","wb")
    arq.write(data)
    arq.close()
    conn.close()
        
def arquivo():
    print 'Fazendo download do arquivo, aguarde...'
    s = urllib.urlopen('http://www.python.org/ftp/python/2.4.2/python-2.4.2.msi')
    data = s.read()
    f = open('C:\\Documents and Settings\\Proprietario\\Desktop\\python-2.4.2.msi', 'wb')
    f.write(data)
    f.close() 

def texto():
    url = "http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/496837/index_txt"
    arq = urllib.urlopen(url)
    open('count_pdf.py', 'w').write(arq.read())

if __name__ == '__main__':
    choice = raw_input('escolha "i", "t" ou "a": ')
    if choice == 'i':
        imagem()
    elif choice == 't':
        texto()
    elif choice == 'a':
        arquivo()
