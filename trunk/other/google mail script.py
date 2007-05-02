# -*- coding: utf-8 -*-

# lib
from smtplib import SMTP
from email.MIMEText import MIMEText
from getpass import getpass
from sys import argv, exit

#except
from smtplib import SMTPAuthenticationError
from smtplib import SMTPRecipientsRefused

# gui
try:
    from Tkinter import Tk
    from gui import EditBoxWindow
except ImportError:
    print "install python-tkinter and gui.py"


def sendmsg(fromg, to, subj):

    tk = Tk()
    app = EditBoxWindow(tk)
    body = MIMEText(app.edit("Edit this..."))
    
    fromg = body["From"] = argv[1]
    to = body["To"] = argv[2]
    subj = body["Subject"] = argv[3]
    body["User-Agent"] = "Google mail script (Python/2.5)"

    server = SMTP("smtp.gmail.com", 587)
    server.set_debuglevel(1)
    
    server.ehlo(fromg)
    server.starttls()
    server.ehlo(fromg)
    
    try:
        passwd = getpass()
        server.login(fromg, passwd)
        
    except SMTPAuthenticationError, exc:
        print 'Login error: %s' % exc
        exit()

    try:
        # todo: unicode error
        server.sendmail(fromg, to, body.as_string())
        print 'Email send ok!'
    except SMTPRecipientsRefused, ex:
        print 'Email send error: %s' % exc
        exit()

if __name__ == '__main__':
    try:
        sendmsg(argv[1], argv[2], argv[3])
    except IndexError:
        print 'run google mail script.py from to subject'
