def aumentar(n, v, formatar=True, m='R$'):
    r = n * (1 + v / 100)
    if formatar:
        return moeda(r, m)
    else:
        return r


def diminuir(n, v, formatar=True, m='R$'):
    r = n * (1 - v / 100)
    if formatar:
        return moeda(r, m)
    else:
        return r


def dobro(n, formatar=True, m='R$'):
    r = n * 2
    if formatar:
        return moeda(r, m)
    else:
        return r


def metade(n, formatar=True, m='R$'):
    r = n / 2
    if formatar:
        return moeda(r, m)
    else:
        return r


def moeda(n, m='R$'):
    return f'{m} {n:.2f}'.replace('.', ',')
