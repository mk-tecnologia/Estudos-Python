'''
Simples programa que separa os digitos de um numero entre 0 e 9999
'''
print('##### CRIE UM PGM QUE SEPARE OS DIGITOS DE UM NUMERO #####')
num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando numero {num}...')
print(f'Unidade = {u}')
print(f'Dezena = {d}')
print((f'Centena = {c}'))
print(f'Milhar = {m}')
