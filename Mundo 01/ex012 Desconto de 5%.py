'''
Simples programa que lê um valor e aplica 5% de desconto
'''
print('##### FAÇA UM PGM QUE LEIA O PREÇO E APLIQUE UM DESCONTO DE 5% #####')
num = float(input('Qual o valor do produto?\n'))
print(f'O Valor {num:.2f} menos 5% de desconto é igual a R${(num - (num * 0.05)):.2f}')
