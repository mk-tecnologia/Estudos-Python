'''
Simples programa que analisa um texto
'''
print('##### CRIE UM PGM QUE FAÇA A ANALISE DE UM TEXTO #####')
texto = str(input('Digite um texto\n')).strip()
print('Analisando seu texto...')
print(f'Seu texto em maisculo: {texto.upper()}')
print(f'Seu texto em minuscula: {texto.lower()}')
print(f'Seu texto tem {(len(texto) - texto.count(" "))} caracteres')
separa = texto.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} caracteres')
