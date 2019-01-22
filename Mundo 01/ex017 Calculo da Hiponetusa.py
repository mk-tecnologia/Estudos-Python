'''
Simples programa que calcula a hipotenusa de um triângulo retangulo
'''
from math import hypot
print('##### CRIE UM PGM QUE CALCULE A HIPOTENUSA DE UM TRIANGULO RETANGULO #####')
co = float(input('Digite o valor do cateto oposto\n'))
ca = float(input('Digite o valor do cateto adjacente\n'))
print(f'Em um triangulo retangulo com cateto oposto de valor {co} e cateto adjacente {ca} o valor da hipotenusa é:'
      f' {hypot(ca, co):.2f}')

