from random import randint


def sorteia(n):
    lst = list()
    for i in range(0, n):
        lst.append(randint(0, 100))
    return lst


def soma_par(lst):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    return soma


lst = sorteia(5)
s = soma_par(lst)

print(f'soma dos pares em {lst} é {s}')
