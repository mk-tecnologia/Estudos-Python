'''
Simples programa que faz o sorteio entre 4 alunos
'''
from random import choice
print('##### CRIE UM PGM QUE SORTEIE ENTRE 4 ALUNOS PARA APAGAR O QUADRO#####')
al1 = input('Digite o nome do aluno 1\n')
al2 = input('Digite o nome do aluno 2\n')
al3 = input('Digite o nome do aluno 3\n')
al4 = input('Digite o nome do aluno 4\n')
lst = [al1, al2, al3, al4]
print(f'O aluno sorteado foi: {choice(lst)}')

