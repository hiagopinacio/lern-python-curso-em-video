def aumentar(n, v):
    r = n * (1 + v / 100)
    return r


def diminuir(n, v):
    r = n * (1 - v / 100)
    return r


def dobro(n):
    r = n * 2
    return r


def metade(n):
    r = n / 2
    return r


def moeda(n, moeda='R$'):
    return f'{moeda} {n:.2f}'.replace('.', ',')
