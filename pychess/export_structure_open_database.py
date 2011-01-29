import sqlite3, os
con = sqlite3.connect('open.db')
with open('openings.sql', 'w') as f:
    for row in con.iterdump(): f.write('%s\n' % row)
