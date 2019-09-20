lista = []

for c in range(0,5):
    lista.append(int(input('Digite um valor inteiro: ')))

menor = min(lista)
maior = max(lista)

if lista.count(menor) > 1:
    print(f'o menor valor é {menor} e aparece nas posições:', end=' ')
    for n, v, in enumerate(lista):
        if menor == v:
            print(n, end = "; ")
else:
    print(f'O menor valor é {menor} e aparece na posição {lista.index(menor)}')
print()
if lista.count(maior) > 1:
    print(f'o maior valor é {maior} e aparece nas posições:', end=' ')
    for n, v, in enumerate(lista):
        if maior == v:
            print(n, end = "; ")
else:
    print(f'O maior valor é {maior} e aparece na posição {lista.index(maior)}')
