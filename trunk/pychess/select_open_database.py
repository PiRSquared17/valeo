import sqlite3, os
con = sqlite3.connect('open.db')
for row in con.execute('select * from openings'): print row
