#!/usr/bin/env python
# -*- coding: utf-8 -*-

from getpass import getpass
from sys import exit, argv
from Tkinter import Tk
from gui import EditBoxWindow

from libgmail import GmailAccount, GmailComposedMessage, GmailSendError, GmailLoginFailure

if __name__ == "__main__":
    try:
        name = argv[1]
    except IndexError:
        name = raw_input("Gmail account name: ")

    pw = getpass("Password: ")
    ga = GmailAccount(name, pw)
    try:
        ga.login()
    except GmailLoginFailure,e:
        print "\nLogin failed. (%s)" % e.message
        sys.exit(1)
    else:
        print "Login successful.\n"

    gmailto = raw_input('Send to: ')
    gmailsubject = raw_input('Subject: ')

    tk = Tk()
    app = EditBoxWindow(tk)
    gmailbody = app.edit('Edit this...')
    
    attach = raw_input('\nSend with attachment? Input filename or empty to continue: ')
    print "\nPlease wait, send message..."
    if attach == '':
        gcm = GmailComposedMessage(gmailto, gmailsubject, gmailbody)
    else:
        gcm = GmailComposedMessage(gmailto, gmailsubject, gmailbody, files=[attach])

    try:
        ga.sendMessage(gcm)
        print "Email send ok!"
    except GmailSendError, ex:
        print '\n%s'%ex
