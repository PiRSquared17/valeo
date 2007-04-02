# -*- coding: utf-8 -*-

# Requer Python e 7zip instalados em seu computador.
# Não testado mas provavelmente funcione: Portable Python e Portable 7zip no seu pendrive.

"""
Verifique:
2. Se o arquivo de backup está sendo usado.
3. Se o pendrive está conectado corretamente.

"""

from time import strftime, localtime
from os import system
from winsound import Beep
from glob import glob
from os.path import getsize
from gui import EditBoxWindow
from Tkinter import Tk

if __name__ == "__main__":
    # data local
    tm = strftime('%d-%m-%Y--%H-%Mhrs', localtime())
    # criando arquivo de compressão 7zip
    # insira a pasta a ser feita a compressão
    system('7z a backup-%s.7z "\\\rede\\root\\path\\another_path"' % tm)
    # teste de integridade
    system('7z t backup-%s.7z' % tm)
    
    fn = 'backup-%s.7z' % tm
    arq = glob(fn)
    tam = 0
    for arqv in arq:
        tam += getsize(arqv)
    #print '%s bytes' % tam
    
    if tam > 200:
        # cópia para pendrive
        system("copy %s E:" % fn)
        # mover para Desktop
        system('move %s "C:\Documents and Settings\Proprietario\Desktop\"' % fn)
        # alerta de encerramento com sucesso
        Beep(1200, 1000) # 1200 Hz em 1 seg
    else:
        system('del backup-%s.7z' % tm)
        tk = Tk()
        app = EditBoxWindow(tk)
        app.edit('\nOcorreu algum erro:\n%s' % __doc__)
