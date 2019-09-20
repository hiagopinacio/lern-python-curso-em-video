lista = ('lapis', 1.00, 'borracha', 2.50, 'caderno', 15.99)

print('='*40)
print(f'{"PREÇOS":^40}')
print('='*40)

for c in range(0, len(lista), 2):
    print(f'{lista[c]:.<30} R$ {lista[c+1]:>5}')
