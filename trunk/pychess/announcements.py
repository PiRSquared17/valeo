#!/usr/bin/env python
# -*- coding: utf-8 -*-

from getpass import getpass
from smtplib import SMTP, SMTPConnectError, SMTPAuthenticationError, SMTPRecipientsRefused
from email.mime.text import MIMEText

mail = 'pychess@gmail.com'
passw = getpass('pychess password: ')
smtp = 'smtp.gmail.com'
to = 'python-announce-list@python.org, pygtk@daa.com.au'
subject = '[ANNOUNCE] PyChess Staunton 0.10'

body = """PyChess is a gtk chess client, originally developed for gnome, but running well under all other linux desktops. (Which we know of, at least). PyChess is 100% python code, from the top of the UI to the bottom of the chess engine, and all code is licensed under the Gnu Public License.

The goal of PyChess is to provide an advanced chess client for linux following the Gnome Human Interface Guidelines. The client should be usable to those new to chess, who just want to play a short game and get back to their work, as well as those who wants to use the computer to further enhance their play.

ery briefly, the following gives a picture of how far we have come. In our minds however, we have only finished 10% of the stuff we want.

* Lets you play against lots of chess engines in the CECP and UCI formats in many different difficulties. The easiest one being very easy. 

* If you like to play against other of the human speices, PyChess supports online play on the FICS servers. 

* Games can be saved in the PGN, EPD and FEN chess fileformats for later continuation or analysis. 

* If you make mistakes or is going for lunch, PyChess lets you undo or pause the game at any time. However if you play online, you need to wait for you opponent to accept the offer. 

* When you are in lack of inspiration, PyChess offers an opening book and so called hint- and spy- arrows, which shows you what the computer would do in your place, and what it would do if you opponent could move just now. 

* Further, PyChess offers a rich and while simple interface, with sound, animation and Human Interface in the main row.

If you would like help fix the translation of PyChess in your language, see http://code.google.com/p/pychess/wiki/RosettaTranslates to get started.

Thanks, PyChess team

* Homepage: http://www.pychess.org
* Project page: http://code.google.com/p/pychess
* Downloads: http://www.pychess.org/download
"""

if __name__ == '__main__':
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = mail
    msg['To'] = to
    try:
        server = SMTP(smtp)
    except SMTPConnectError, ex:
        print '\n%s'%ex
    print '\nConnecting to Gmail account...'
    try:
        server.login(mail, passw)
    except SMTPAuthenticationError, ex:
        print '\n%s'%ex
    print 'Sending message...'
    try:
        server.sendmail(mail, to, msg.as_string())
    except SMTPRecipientsRefused, ex:
        print '\n%s'%ex
    print 'Email send ok.'
    server.quit()
