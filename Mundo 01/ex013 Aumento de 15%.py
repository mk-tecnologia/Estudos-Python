'''
Simples programa que lê um valor e aplica um aumento de 15%
'''
print('##### FAÇA UM PGM QUE LEIA O VALOR DO SALARIO E DE UM AUMENTO DE 15% #####')
num = float(input('Qual o valor do salario?\n'))
print(f'o salario de R${num:.2f} com 15% de aumento é igual a R${(num + (num * 0.15)):.2f}')
