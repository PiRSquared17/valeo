#!/usr/bin/env python
# -*- coding: utf-8 -*-

from getpass import getpass
from smtplib import SMTP, SMTPException
from StringIO import StringIO
from MimeWriter import MimeWriter
from base64 import encode
from mimetypes import guess_type
from sys import exit, argv
from socket import gaierror

def sendmail(attach):
    mail = raw_input(u'Email: ')
    user = raw_input('User: ')
    passw = getpass('Password mail: ')
    serv = raw_input(u'SMTP server: ')
    to = raw_input(u'Send To: ')
    subj = raw_input(u'Subject: ')
    bodymsg = raw_input(u'Message body: ')
    attach = [attach]
    print '\nPlease wait, send message...'
    try:
        server = SMTP(serv)
    except gaierror:
        print (u'\nYour SMTP address error or internet socket error.')
        exit()
    try:
        server.login(user, passw)
        print "\nPlease wait, send message..."
        message = StringIO()
        writer = MimeWriter(message)
        writer.addheader('From', mail)
        writer.addheader('To', to)
        writer.addheader('Subject', subj)
        #writer.addheader('User-Agent', 'valeo mail script (Python/2.5)')
        writer.startmultipartbody('mixed')
        part = writer.nextpart()
        body = part.startbody('text/plain')
        body.write(bodymsg)
        for att in attach:
            part = writer.nextpart()
            part.addheader('Content-Transfer-Encoding', 'base64')
            part.addheader('Content-Disposition', 'attachment; filename="' + str(att) + '"')
            body = part.startbody(guess_type(str(att))[0])
            encode(open(str(att), 'rb'), body)
        writer.lastpart()
        server.sendmail(mail, to, message.getvalue())
        print 'Send ok!'
        server.quit()
    except SMTPException, ex:
        print '\n%s'%ex

def main():
    try:
        attach = argv[1]
    except:
        print (u'\nRun: python %s filename' % argv[0])
        exit()
    try:
        sendmail(attach)
    except KeyboardInterrupt:
        print '\n'

if __name__ == '__main__':
    main()
