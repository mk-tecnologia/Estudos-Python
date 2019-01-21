'''
Simples Programa que lê um numero e informa o dobro, triplo e raiz quadrada dele
'''
print('##### FAÇA UM PGM QUE LEIA UM NUMERO E MOSTRE SEU DOBRO, TRIPLO E A RAIZ QUADRADA #####')
num = float(input('Qual o valor?\n'))
print(f'Odobro de {num} é igual a {num * 2}')
print(f'o triplo de {num} é igual a {num * 3}')
print(f'a raiz quadrada de {num} é {num**(1 / 2):.2f}')
print(f'a raiz quadrada de {num} calculada de com a função pow deu {pow(num, 1 / 2):.2f}')
