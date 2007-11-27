# -*- coding: utf-8 -*-

import MySQLdb as mysql

db = mysql.connect(host="localhost", user="root", passwd='12', db="test")
cursor = db.cursor()
cursor.execute ("DROP TABLE IF EXISTS carro")
cursor.execute ("CREATE TABLE carro (nome CHAR(20), marca CHAR(20), cor CHAR(10));")

i = 1
print ('Detalhes do carro')
print '-'*17

escolha = True
while escolha:
    carro_nome = raw_input('Carro %s: ' % i) 
    carro_marca = raw_input('Marca %s: ' % i)
    carro_cor = raw_input('Cor %s: ' % i)
    cursor.execute ("INSERT INTO carro (nome, marca, cor) VALUES ('%s', '%s', '%s');" % (carro_nome, carro_marca, carro_cor))
    i+=1
    sair = raw_input(u'Incluir mais carros (S)im ou (N)ão: ')
    if sair in ['S', 's']:
        escolha = True
    else:
        escolha = False
        break

cursor.execute ("SELECT * FROM carro")
while (1):
    row = cursor.fetchone()
    if row == None:
        break
    print "Carro: %s, %s, %s" % (row[0], row[1], row[2])
cursor.close()
db.commit()
db.close()
