#!/usr/bin/env python
'''
delete_all.py -- Demo to delete all messages in folder
License: GPL 2.0
Copyright 2006 leogregianin@users.sourceforge.net
'''

import sys
from getpass import getpass
import libgmail

if __name__ == "__main__":
    try:
        name = sys.argv[1]
    except IndexError:
        name = raw_input("Gmail account name: ")
        
    pw = getpass("Password: ")

    ga = libgmail.GmailAccount(name, pw)

    print "\nPlease wait, logging in..."

    try:
        ga.login()
    except libgmail.GmailLoginFailure,e:
        print "\nLogin failed. (%s)" % e.message
        sys.exit(1)
    else:
        print "Login successful.\n"

    FOLDER_list = raw_input('Choose a folder (inbox, starred, all, drafts, sent, spam): ')
    folder = ga.getMessagesByFolder(FOLDER_list, allPages=True)

    choice = raw_input('\nDo you really delete all messages in folder? [yes/no] ')
    if choice in ['yes', 'y']:
        for thread in folder:
            print thread.id, len(thread), thread.subject, 'delete ok!\n'
            ga.trashThread(thread)
    print '\nDelete all messages in folder sucessful!\n'
