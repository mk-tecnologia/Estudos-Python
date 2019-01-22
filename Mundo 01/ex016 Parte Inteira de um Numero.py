'''
Simples programa que retorna a parte inteira de um valor
'''
from math import trunc
print('##### CRIE UM PGM QUE LEIA UM NUMERO REAL E MOSTRE SOMENTE SUA PARTE INTEIRA #####')
num = float(input('Digite um numero\n'))
print('Resultado com a função TRUNC')
print(f'Você digitou {num} e a parte inteira dele é {trunc(num)}')
print('Resultado com a função INT')
print(f'Você digitou {num} e a parte inteira dele é {int(num)}')
