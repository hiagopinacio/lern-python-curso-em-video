num = [2, 5, 9, 1]
print('*'*80)
print(f'{"Listas em Python":^80}')
print('*'*80+'\n')

print(f'Lista Considerada: {num}')
num[2] = 3 #listas são mutaveis
print(f'Listas são mutáveis. Trocando intem da posição 2: {num}')
num.append(7)
print(f'Adicionando valores no final da lista com append(valor): {num}')
num.insert(3, 15)
print(f'Adicionando valores na meio da lista com insert(pos, valor): {num}')
num.sort()
print(f'Colocando a lista em ordem (sort): {num}')
num.sort(reverse=True)
print(f'Colocando a lista em ordem decrescent (sort(reverse=True)): {num}')
print(f'Essa lista tem {len(num)} elementos (len)')

print('_'*80)
print(f'{"Eliminando Elementos":^80}\n')
num.pop(0)
print(f'Eliminando elemento da posição 0 (pop(0)): {num}')
del num[3]
print(f'Eliminando elemento da posição 3 (pop(0)): {num}')

if 5 in num:
    num.remove(5)
print(f'Eliminando elemento 5 se existir (IF 5 in LISTA: LISTA.remove(5)): {num}')

print('_'*80)
print(f'{"ENUMERATE":^80}\n')
print('ENUMERATE É MUITO FODA, pega valor e posição em um FOR:')
for c, n in enumerate(num):
    print(f'    Valor {n} na posição {c}')

print('_'*80)
print(f'{"Copiando Listas":^80}\n')

a = [2, 3, 5, 8, 9, 4]
print(f'lista considerada: {a}')
b = a
a[2] = 10
print(f'atribuindo lista a a lista b (b = a), se mudar um valor em a, também muda em b:\n   {a}\n   {b}')
c = a[:]
a[2] = 5
print(f'Para copiar sem linkar deve-se usar fatiamento (c=a[:]):\n   {a}\n   {c}')