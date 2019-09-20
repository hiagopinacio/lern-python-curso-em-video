#TUPLAS SAO IMUTAVEIS

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(f'exibindo de [0:3]: {lanche[0:3]}')
print(f'exibindo de [-1::-1]: {lanche[-1::-1]}')

print('\n FOR da tupla simples\n')
for comida in lanche:
    print(comida)

print('\n FOR da tupla com contador (range)\n')
for cont in range(0,len(lanche)):
    print(f'{lanche[cont]} na porsição {cont}')

print('\n FOR da tupla com enumerate\n')
for pos, comida in enumerate(lanche):
    print(f'{comida} na porsição {pos}')

print('\n\n')
a= (2,4,5)
b=( 5, 3, 2, 9, 0)
c=a+b
print(f'a = {a}')
print(f'b = {b}')
print(f'c = a+b = {c}')
print(f'c.count(5): {c.count(5)}')
print(f'c.index(2): {c.index(2)}')
print(f'index de 2 a partir da pos 1 (c.index(2,1)): {c.index(2,1)}') #index de 2 a partir da pos 1
print(f'ordenado (sorted): {sorted(c)}')
print(f'maximo: {max(c)}')
print(f'minimo: {min(c)}')
