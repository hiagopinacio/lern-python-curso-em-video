# MANIPULAÇÃO DE TEXTO

#posição 012345678901234567890
frase = 'Curso em Vídeo Python'
print('frase >>'+frase)

#FATIAMENTO
print('\n FATIAMENTO \n')

print('pegando um caractere na posição 9 >>', end='')
print(frase[9])

print('pegando uma serie de caracteres de 6 a 13 [6:13] >>', end='')
print(frase[5:13])

print('pegando uma serie de caracteres de 6 a 13 de 2 em 2 [6:13:2] >>', end='')
print(frase[5:13:2])

print('pegando uma serie de caracteres do início até posição 5 [:5] >>', end='')
print(frase[:5])

print('pegando uma serie de caracteres da posição 15 até o final [15:] >>', end='')
print(frase[15:])

print('pegando uma serie de caracteres da posição 9 até o final de 3 em 3 [9::3] >>', end='')
print(frase[9::3])

# ANÁLISE
print('\n ANÁLISE \n')

print('comprimento da frase >>', end='')
print(len(frase))

print('contando quantos "o"s tem na frase >>', end='')
print(frase.count('o'))

print('contando quantos "o"s tem na frase entre posições 0 e 13 >>', end='')
print(frase.count('o',0,13))

print('contando quantos "x"s tem na frase  >>', end='')
print(frase.count('x'))

print('procurando a posição de um ou mais caracteres (ex: deo) >>', end='')
print(frase.find('deo'))

print('procurando a posição de um ou mais caracteres que não tem na frase (ex: x) >>', end='')
print(frase.find('x'))

print('procurando se existe um ou mais caracteres na frase (ex: x) >>', end='')
print('x'in frase)

print('procurando se existe um ou mais caracteres na frase (ex: urs) >>', end='')
print('urs'in frase)

#TRASNFORMAÇÃO

print('\n TRANSFORMAÇÕES \n')

print('alterando "Curso" por "Aula" na frase (replace)', end='>>')
print(frase.replace('Curso','Aula'))

print('colocando a frase em maiúscula (upper)', end='>>')
print(frase.upper())

print('colocando a frase em minúcula (lower)', end='>>')
print(frase.lower())

print('colocando a primeira letra da frase em maíuscula e o restante em minúcula (captalize)', end='>>')
print(frase.capitalize())

print('colocando a primeira letra de cada palavra em maíuscula e o restante em minúcula (title)', end='>>')
print(frase.title())

print('trocando maiusculas e minúsculas (swapcase)', end='>>')
print(frase.swapcase())

frase2= '   Aprendento Python  '
print('\n nova frase analizada >>{}\n'.format(frase2))

print('removendo espaços desnecessários no início e fim da frase (strip)', end='>>')
print(frase2.strip())

print('removendo espaços desnecessários no início da frase (lstrip)', end='>>')
print(frase2.lstrip())

print('removendo espaços desnecessários no fim da frase (rstrip)', end='>>')
print(frase2.rstrip())

print('\n DIVISÃO \n')
lista = frase.split()

print('dividindo a frase em palavras (split) ', end = '>>' )
print(frase.split())

print("juntando uma lista de stings com - ('-'.join(lista))", end='>>')
print('-'.join(lista))