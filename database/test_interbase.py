import kinterbasdb as k
import sys

k.init(type_conv=200)
# Never imports mx.DateTime:
# assert 'mx' not in sys.modules

con = k.connect(dsn='c:/test.gdb', user='sysdba', password='masterkey')
cur = con.cursor()

sql = '''
create table brazil_election_2006
(
  name    varchar(20),
  cod     integer
);
'''

cur.execute(sql)
con.commit()

sql2 = '''
insert into brazil_election_2006 (name, cod) values ('Lula', 13);
insert into brazil_election_2006 (name, cod) values ('Alkmin', 45);
'''
cur.execute(sql)
con.commit()

find = 'select name, year_released from languages order by year_released'

for fieldDesc in cur.description:
    print fieldDesc[k.DESCRIPTION_NAME].ljust(fieldDesc[k.DESCRIPTION_DISPLAY_SIZE]) ,
print 
print '-' * 78

fieldIndices = range(len(cur.description))
for row in cur:
    for fieldIndex in fieldIndices:
        fieldValue = str(row[fieldIndex])
        fieldMaxWidth = cur.description[fieldIndex][k.DESCRIPTION_DISPLAY_SIZE]

        print fieldValue.ljust(fieldMaxWidth) ,

    print 
