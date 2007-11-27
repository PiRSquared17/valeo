# -*- coding: utf-8 -*-

import httplib, urllib

def arquivo():
    s = urllib.urlopen('http://www.python.org/ftp/python/2.4.2/python-2.4.2.msi')
    data = s.read()
    f = open('C:\\Documents and Settings\\Administrador\\Desktop\\python-2.4.2.msi', 'wb')
    f.write(data)
    f.close() 

if __name__ == '__main__':

    from progressbar import *
    widgets = ['Test: ', Percentage(), ' ', Bar(marker=RotatingMarker()),' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=20000000).start()
    #for i in range(2000000):
    #    pbar.update(10*i+1)
    arquivo()
    pbar.finish()
