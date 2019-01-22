'''
Simples programa que lê a quantidade de KM pecorridos e dias e calcula o valor a ser pago
'''
print('##### FAÇA UM PGM QUE LEIA A QTDADE DE KM PECORRIDOS E A QTDADE DE DIAS E CALCULE O PREÇO A PAGAR #####')
print('##### ALUGUEL CARRO CUSTA R$60 POR DIA E R$0,15 PORR KM RODADO #####')
d = int(input('Quantos dias de aluguel?\n'))
km = float(input('Quantos km rodados?\n'))
print(f'O carro foi alugado {d} dias e rodou {km}km e o total a pagar é de R${((d * 60) + (km * 0.15)):.2f}')
