'''
Simples programa que calcula a quantidade de tinta necessária para pintar uma parede
'''
print('##### FAÇA UM PGM QUE CALCULE A ÁREA DE UMA PAREDE EM M E DIGA A QTDADE DE TINTA PARA PINTA-LA (1L = 2M2) #####')
alt = float(input('Qual a altura da parede?\n'))
lag = float(input('Qual a largura da parede?\n'))
print(f'A parede tem uma área de {alt * lag:.2f}m e serão necessários {alt * lag / 2:.2f}litros de tinta para a pintura dela')
