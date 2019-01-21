'''
Simples Programa que traz informaçoões sobre um dado fornecido
'''
print('##### FAÇA UM PGM QUE DIGA O TIPO DELE E TODAS AS INFORMAÇÕES POSSÍVEIS #####')
dado = input('Digite Algo:\n')
print(f'Você digitou: {dado}')
print(f'{dado} é do tipo primitivo {type(dado)}')
print(f'{dado} é um numero? {dado.isnumeric()}')
print(f'{dado} é somente um espaço? {dado.isspace()}')
print(f'{dado} é somente letras {dado.isalpha()}')
print(f'{dado} é somente alfanumerico? {dado.isalnum()}')
print(f'{dado} está em maiuscula? {dado.isupper()}')
print(f'{dado} está em miniscula? {dado.islower()}')
print(f'{dado} está capitalizada? {dado.istitle()}')
