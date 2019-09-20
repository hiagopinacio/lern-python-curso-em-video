lista = []
lista.append(int(input('Digite um valor inteiro para inicar a lista: ')))
c=1
while c < 5:
    valor = (int(input('Digite outro valor inteiro: ')))
    menor = min(lista)
    maior = max(lista)

    if valor in lista:
        print(f'O valor {valor} já foi adicionado anteriormente e não será considerado')

    elif valor < menor:
        lista.insert(0, valor)
        print(f'O valor {valor} foi adicionado no início da lista, na posiçao 0')
        c += 1

    elif menor < valor < maior:
        for pos, vlist in enumerate(lista):
            if vlist > valor:
                lista. insert(pos, valor)
                print(f'O valor {valor} foi adicionado na posição {pos} da lista')
                c += 1
                break

    elif valor > maior:
        print(f'O valor {valor} foi adicionado no final da lista na posição {len(lista)}')
        lista.append(valor)
        c += 1

print(f'lista: {lista}')
