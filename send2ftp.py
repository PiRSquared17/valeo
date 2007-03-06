#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ftplib import FTP
from getpass import getpass
from sys import exit, argv
from socket import gaierror

ftpserver = 'ftp.consisa.inf.br'
ftpuser = '92200199'
ftppw = getpass('FTP password: ')
print 'Connecting to %s...\n' % ftpserver
try:
    ftp = FTP(ftpserver)
except gaierror:
    print 'Your FTP address error or internet socket error.'
    exit()
try:
    ftp.login(ftpuser, ftppw)
except:
    print '\nConnection failure!'
    exit()
print 'Your FTP server has:\n'
ftp.retrlines('LIST')
try:
    filetransfer = 'send2ftp.py' # nome do arquivo
    print ('Sending %s...' % filetransfer)
    ftp.storbinary('STOR ' + filetransfer, open(filetransfer, 'rb'), 8192)
    print "Send ok!\n"
    print 'And now, FTP server has:\n'
    ftp.retrlines('LIST')
    ftp.quit()
except KeyboardInterrupt:
    print '\n'

