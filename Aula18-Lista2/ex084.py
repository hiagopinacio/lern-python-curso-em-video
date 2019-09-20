lista = []
pessoa = []

while True:
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(float(input('Digite o peso: ')))
    lista.append(pessoa[:])
    pessoa.clear()
    continua = input('Continuar [s]? ')
    if continua not in 'Ss':
        break

print(f'\n\n{len(lista)} foram cadastradas')

ordemPeso = [lista[0]]
maior = lista[0][1]

for p in range(1, len(lista)):
    if lista[p][1] >= maior:
        ordemPeso.append(lista[p])
        maior = lista[p][1]
    else:
        for i, x in enumerate(ordemPeso):
            if lista[p][1] < x[1]:
                ordemPeso.insert(i, lista[p])
                break
print(f'\n{"PESSOAS POR ORDEM DE PESO":*^50}\n')

for x in ordemPeso:
    print(f'{x[0]:.<40}{x[1]:>10}')
