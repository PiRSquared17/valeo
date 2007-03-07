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
choice = raw_input("\nDo you want (s)end or (d)ownload to ftp? ")
if choice in ['s', 'S']:
    try:
        filetransfer = raw_input("What filename do you want to send (p.e.: readme.txt)? ")
        print ('Sending %s...' % filetransfer)
        ftp.storbinary('STOR ' + filetransfer, open(filetransfer, 'rb'), 8192)
        print "Send ok!\n"
        print 'And now, FTP server has:\n'
        ftp.retrlines('LIST')
        ftp.quit()
    except KeyboardInterrupt:
        print '\n'
        
elif choice in ['d', 'D']:
    try:
        filedownload = raw_input("What filename do you want to download (p.e.: readme.txt)? ")
        ftp.retrbinary(('RETR %s' % filedownload), open(filedownload, 'wb').write)
        print "Download ok!\n"
        ftp.quit()
    except KeyboardInterrupt:
        print '\n'
else:
    print 'input certain code... quit'
    exit()

