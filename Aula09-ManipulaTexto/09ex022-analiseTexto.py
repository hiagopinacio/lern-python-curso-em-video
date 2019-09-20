#022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao  todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome=input('digite seu nome\n').strip()
print('seu nome com todas as letras maiúsculas:', nome.upper())
print('seu nome com todas as letras minúsculas:', nome.lower())
print('seu nome possui {} letras sem espaços'.format(len(nome)-nome.count(' ')))
dividido = nome.split()
print('seu primeiro nome {} tem {} letras'.format(dividido[0],len(dividido[0])))
