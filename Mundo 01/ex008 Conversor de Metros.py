'''
Simples programa de conversão de metros
'''
print('##### FAÇA UM PGM QUE LEIA UMA MEDIDA EM METROS E CONVERTA PRA CM E MM #####')
m = float(input('Digite a medida em metros:\n'))
print(f'A medida {m}m é equivalente a:')
print(f'{m * 0.001}km (kilometros)')
print(f'{m * 0.01}hm (hectometros)')
print(f'{m * 0.1:.1f}dam (decametros)')
print(f'{m * 10:.0f}dm (decimetros)')
print(f'{m * 100:.0f}cm (centrimetros)')
print(f'{m * 1000:.0f}mm (milimetros)')
