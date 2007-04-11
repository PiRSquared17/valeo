# -*- coding: utf-8 -*-
"""
Este módulo não verifica anos, portanto, não verifica
anos bissestos. O mês de Fevereiro é sempre contado
com 28 dias.

Em Python, o índice sempre começa em zero, portanto,
o primeiro elemento é zero, o segundo é um, etc.

Funções:

DiadoAno(dia, mês)     : Retorna um dia do ano.

                         >>> import daylib
                         >>> daylib.DiaDoAno(28, 0)
                         29 de Janeiro
                         >>>

DiasDoMes(mês)         : Retorna todos os dias de um mês.

                         >>> import daylib
                         >>> daylib.DiasDoMes(1)
                         1 de Fevereiro
                         2 de Fevereiro
                         ...
                         28 de Fevereiro
                         >>>

TodosOsDias()          : Retorna todos os dias no ano.
                         >>> import daylib
                         >>> daylib.TodosOsDias()
                         1 de Janeiro
                         ...
                         31 de Dezembro
                         >>>

TODO:
* suporte a anos -> anos bissextos 

"""

dias31 = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
          '10', '11', '12', '13', '14', '15', '16',
          '17', '18', '19', '20', '21', '22', '23',
          '24', '25', '26', '27', '28', '29', '30', '31']

dias30 = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
          '10', '11', '12', '13', '14', '15', '16',
          '17', '18', '19', '20', '21', '22', '23',
          '24', '25', '26', '27', '28', '29', '30']

dias28 = ['1', '2', '3', '4', '5', '6', '7', '8',
          '9', '10', '11', '12', '13', '14', '15',
          '16', '17', '18', '19', '20', '21', '22',
          '23', '24', '25', '26', '27', '28']

meses = [' de Janeiro', ' de Fevereiro', u' de Março', ' de Abril',
         ' de Maio', ' de Junho', ' de Julho', ' de Agosto',
         ' de Setembro', ' de Outubro', ' de Novembro', ' de Dezembro']

def DiaDoAno(dia, mes):
    for d in xrange(1):
        if mes in [0, 2, 4, 6, 7, 9, 11]:
            print dias31[dia]+meses[mes]
        elif mes in [1]:
            print dias28[dia]+meses[mes]
        elif mes in [3, 5, 8, 10]:
            print dias30[dia]+meses[mes]

def DiasDoMes(mes):
    dia = 0
    if mes in [0, 2, 4, 6, 7, 9, 11]:
        for d in xrange(31):
            print dias31[dia]+meses[mes]
            dia = dia+1
    elif mes in [1]:
        for d in xrange(28):
            print dias28[dia]+meses[mes]
            dia = dia+1
    elif mes in [3, 5, 8, 10]:
        for d in xrange(30):
            print dias30[dia]+meses[mes]
            dia = dia+1
	
def TodosOsDias():
    pass

if __name__ == '__main__':
    #DiaDoAno(1, 2)
    #DiasDoMes(11)
    TodosOsDias()
