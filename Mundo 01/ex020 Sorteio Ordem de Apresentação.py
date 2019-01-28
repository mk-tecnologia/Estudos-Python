'''
Simples programa que crie uma ordem de apresentação de alunos
'''
from random import shuffle
print('##### CRIE UM PROGRAMA QUE FAÇA A ORDEM DE APRESENTAÇÃO ENTRE 4 ALUNOS #####')
al1 = input('Digite o nome do aluno 1\n')
al2 = input('Digite o nome do aluno 2\n')
al3 = input('Digite o nome do aluno 3\n')
al4 = input('Digite o nome do aluno 4\n')
lst = [al1, al2, al3, al4]
shuffle(lst)
print(f'A ordem de apresentação será a seguinte:\n {lst}')
