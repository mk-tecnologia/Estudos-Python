'''
Simples programa que lê uma ângulo e retorna seu seno, cosseno e tangente
'''
from math import cos, sin, tan, radians
print('##### CRIE UM PGM QUE LEIA UM ANGULO E MOSTRE O VALOR DO SENO, COSSENO E TANGENTE #####')
ang = float(input('Qual o valor do Angulo?\n'))
print(f'O angulo {ang} tem seno de {sin(radians(ang)):.2f}')
print(f'O angulo {ang} tem cosseno de {cos(radians(ang)):.2f}')
print(f'O angulo {ang} tem tangende de {tan(radians(ang)):.2f}')
